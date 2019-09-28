from django.shortcuts import render
from django.http import HttpResponse
from django.template import context,loader
import sqlite3
from Quizz.models import institute
from Quizz.models import student
from Quizz.models import quizset
from Quizz.models import quizresults
from Quizz.models import teacher
from datetime import datetime
from datetime import date


def index(request):
	t=loader.get_template("index.html")
	c={}
	v=t.render(c)
	resp=HttpResponse(v)
	return(resp)
def register(request):
	return render(request,'register.html')

def instituteSave(request):
	Uid=request.POST["uid"]
	password=request.POST["password"]
	cpwd=request.POST["cpwd"]
	insttype=request.POST["insttype"]
	address=request.POST["address"]
	city=request.POST["city"]
	contactno=request.POST["contactno"]
	u=institute(userid=Uid,password=password,insttype=insttype,address=address,city=city,contactno=contactno)
	u.save()
	a="<h1>Record Saved </h1>"
	resp=HttpResponse(a)
	return(resp)
def login(request):
	return render (request,'login.html')
def instituteLogin(request):
	return render(request,'instituteLogin.html')
def studentLogin(request):
	return render(request,'studentLogin.html')
def instituteLoginCheck(request):
	userid=request.POST["userid"]
	password=request.POST["password"]
	#a=HttpResponse(password)
	#return(a)
	qs=institute.objects.filter(userid=userid,password=password)
	if qs:
		request.session['userid']=userid
		request.session['password']=password
		return render(request,"instituteHome.html",{"uname":qs[0].instname})
	else:
		msg="<h1>Invalid User ID or Password </h1>"
		resp=HttpResponse(msg)
		return(resp)
def studentLoginCheck(request):
	userid=request.POST["userid"]
	password=request.POST["password"]
	qs=student.objects.filter(userid=userid,password=password)
	if qs:
		request.session['userid']=userid
		request.session['password']=password
		return render(request,"studenthome.html",{"uname":qs[0].studentname})
	else:
		msg="<h1>Invalid User ID or Password </h1>"
		resp=HttpResponse(msg)
		return(resp)
def changePassword_institute(request):
	return render(request,'changePassword_institute.html')
def changePassword_student(request):
	return render(request,'changePassword_student.html')
def changePassword_teacher(request):
	return render(request,'changePassword_teacher.html')
def changePasswordSave_institute(request):
	eid=request.session.get('userid')
	pwd=request.session.get('password')
	op=request.POST['op']
	np=request.POST['np']
	qs=institute.objects.filter(userid=eid)
	if pwd==op and qs:
		qs[0].Password=np
		qs[0].save()
		msg="<h1>PASSWORD CHANGED SUCCESSFULLY</H1>"
	else:
		msg="<h1>INVALID PASSWORD</h1>"
	resp=HttpResponse(msg)
	return(resp)
def changePasswordSave_student(request):
	eid=request.session.get('userid')
	pwd=request.session.get('password')
	op=request.POST['op']
	np=request.POST['np']
	qs=student.objects.filter(userid=eid)
	if pwd==op and qs:
		qs[0].Password=np
		qs[0].save()
		msg="<h1>PASSSWORD CHANGED SUCCESSFULLY</H1>"
	else:
		msg="<h1>INVALID PASSWORD</h1>"
	resp=HttpResponse(msg)
	return(resp)
def changePasswordSave_teacher(request):
	eid=request.session.get('userid')
	pwd=request.session.get('password')
	op=request.POST['op']
	np=request.POST['np']
	qs=teacher.objects.filter(userid=eid)
	if pwd==op and qs:
		qs[0].Password=np
		qs[0].save()
		msg="<h1>PASSWORD CHANGED SUCCESSFULLY</H1>"
	else:
		msg="<h1>INVALID PASSWORD</h1>"
	resp=HttpResponse(msg)
	return(resp)
	
def signout(request):
	request.session.flush()
	return render(request,'index.html')
def addstudent(request):
	return render(request,'student.html')

def studentSave(request):
	Uid=request.POST["eid"]
	password=request.POST["pwd"]
	cpwd=request.POST["cpwd"]
	insttype=request.POST["instname"]
	gen=request.POST["gen"]
	name=request.POST["unm"]
	dob=request.POST["dob"]
	u=student(userid=Uid,password=password,instname=insttype,gender=gen,birthdate=dob,studentname=name)
	u.save()
	a="<h1>Record Saved </h1>"
	resp=HttpResponse(a)
	return(resp)
def questionSetup(request):
	return render(request,'questionSetup.html')

def questionSetupSave(request):
	ques=request.POST["ques"]
	a1=request.POST["a1"]
	a2=request.POST["a2"]
	a3=request.POST["a3"]
	a4=request.POST["a4"]
	ca=request.POST["ca"]
	#marks=request.POST["marks"]
	uid=request.session.get("userid")
	qs=institute.objects.filter(userid=uid)
	inm=qs[0].instname
	q=quizset(instname=inm,gues=ques,answer1=a1,answer2=a2,answer3=a3,answer4=a4,correctanswer=ca)
	q.save()
	return render(request,"questionSetup.html")


def checkQuestion(request):
	ques=request.GET["ques"];
	qs=QuizQuestion.objects.filter(Question=ques)
	if qs:
		msg="Question already exists "
	else:
		msg="Question doesn't exist"
	resp=HttpResponse(msg)
	return(resp)

def questionBank(request):
	userid=request.session.get("userid")
	q=institute.objects.filter(userid=userid)
	inm=q[0].instname
	qs=quizset.objects.filter(instname=inm)
	o="<table width='100%' border='1'>"
	o+="<tr>"
	o+="<th>Delete</th>"
	o+="<th> Question</th>"
	o+="<th>Answer 1</th>"
	o+="<th>Answer 2</th>"
	o+="<th>Answer 3</th>"
	o+="<th>Answer 4</th>"
	o+="<th>Correct Answer</th></tr>"
	for rec in qs:
		o+="<tr>"
		o+="<td><a href=delQuestion?qid="+str(rec.id)+" >Delete</a></td><td align=center>"+rec.gues+"</td>"
		o+="<td align=center>"+rec.answer1+"</td>"
		o+="<td align=center>"+rec.answer2+"</td>"
		o+="<td align=center>"+rec.answer3+"</td>"
		o+="<td align=center>"+rec.answer4+"</td>"
		o+="<td align=center>"+rec.correctanswer+"</td></tr>"
	o+="</table>"
	resp=HttpResponse(o)
	return(resp)
def delQuestion(request):
	qid=request.GET["qid"]
	rs=quizset.objects.filter(id=qid).delete()
	v=questionBank(request)
	resp=HttpResponse(v)
	return(resp)
	
def startQuiz(request):
	v='''
<html>
<head>
<style>

#button1 {
  background-color: white;
  color: black;
  border: 2px solid #4CAF50; /* Green */
}
#button2 {
  background-color: white; 
  color: black; 
  border: 2px solid #008CBA;
}

#button3 {
  background-color: white; 
  color: black; 
  border: 2px solid #f44336;
}

</style>
<meta charset="utf-8"/>
<meta name="viewport" content="width=device-width,initial-scale=1"/>
<link rel="stylesheet" href="/static/bootstrap.min.css"/>
<script src="/static/jquery.min.js"></script>
<script src="/static/bootstrap.min.js"></script>
<script>
$(document).ready(function(){
ques=$(".ques");
tq=ques.length;
tm=tq*10
a=tm
k=setInterval(function(){
a--;
msg="Time Left: "+a 
$("#timer").text(msg);
if(a<=30)
$("#timer").css("background-color","red");
if(a==1)
{
clearInterval(k);
document.quizForm.submit();
}
},1000)


$(".nextQ").click(function(){
qno=$(this).val();
if(qno<tq-1)	
{
$(this).parent().hide();
$(this).parent().next().show();
}
})
$(".prevQ").click(function(){
qno=$(this).val();
if(qno>0)
{
$(this).parent().hide();
$(this).parent().prev().show();
}
})


});
	</script>
	</head>
	<body>
	<h3 id=timer align=center width=50% >Time Left: </h3>
<form name=quizForm method=get action=quizsave >
'''
	eid=request.session.get("userid")
	s=student.objects.filter(userid=eid)
	inm=s[0].instname
	qs=quizset.objects.filter(instname=inm)
	i=0
	for rec in qs:
		if i==0:
			v+="<div class='ques jumbotron'  style='display:block' >Ques: "+rec.gues
		else:
			v+="<div class='ques' style='display:none' >Ques: "+rec.gues
		v+="</br>"
		v+="<input type=radio name='ans"+str(i)+"' value='A' />"+rec.answer1+"</br>"
		v+="<input type=radio name='ans"+str(i)+"' value='B' />"+rec.answer2+"</br>"
		v+="<input type=radio name='ans"+str(i)+"' value='C' />"+rec.answer3+"</br>"
		v+="<input type=radio name='ans"+str(i)+"' value='D' />"+rec.answer4+"</br>"
		v+="<input type=radio name='ans"+str(i)+"' value='0' checked />"+rec.answer4+"</br>"
		v+="<button type=button class='nextQ form-control ' id='button1' value="+str(i)+" >Next Question</button> "
		v+="<button type=button class='prevQ form-control' id='button2' value="+str(i)+">Previous Question</button> "
		v+="</div>"
		i=i+1
	v+="<input type=submit value=submit class='prevQ form-control' style='background-color: white;  color: black; border: 2px solid #f44336;'>"
		
	v+="</form>"
	v+="</body>"
	resp=HttpResponse(v)
	return(resp)

def profile(request):
	eid=request.session.get("userid")
	s=student.objects.filter(userid=eid)
	v="<table width='70%'>"
	v+="<tr><td>Institute Name</td><td>"+s[0].instname+"</td></tr>"
	v+="<tr><td> Student Name </td> <td>"+ s[0].studentname+" </td></th>"
	v+="<tr><td>Student Email </td><td>"+s[0].userid+" </td></tr>"
	v+="<tr><td>Gender </td><td>"+s[0].gender+" </td></tr>"
	v+="<tr><td>DOB </td><td>"+str(s[0].birthdate)+" </td></tr>"
	#v+="<tr><td>Address </td><td>"+s[0].address+" </td></tr>"
	v+="</table>"
	resp=HttpResponse(v)
	return(resp)
def profile_teacher(request):
	eid=request.session.get("userid")
	s=teacher.objects.filter(userid=eid)
	v="<table width='70%'>"
	v+="<tr><td>Institute Name</td><td>"+s[0].instname+"</td></tr>"
	v+="<tr><td> Student Name </td> <td>"+ s[0].name+" </td></th>"
	v+="<tr><td>Student Email </td><td>"+s[0].userid+" </td></tr>"
	v+="<tr><td>Gender </td><td>"+s[0].gender+" </td></tr>"
	v+="<tr><td>DOB </td><td>"+str(s[0].birthdate)+" </td></tr>"
	#v+="<tr><td>Address </td><td>"+s[0].address+" </td></tr>"
	v+="</table>"
	resp=HttpResponse(v)
	return(resp)
	
def quizsave(request):
	eid=request.session.get("userid")
	s=student.objects.filter(userid=eid)
	inm=s[0].instname
	qs=quizset.objects.filter(instname=inm)
	corr=0
	v="<table width='100%' border='1'>"
	v+="<tr>"
	v+="<th>Sr No</th>"
	v+="<th>Correct Answer</th>"
	v+="<th>Your Answer</th>"
	v+="<th>Correct/Incorrect</th></tr>"
	
	for i in range(0,len(qs)):
		ca=qs[i].correctanswer;
		ua=request.GET["ans"+str(i)]
		v+="<tr>"
		v+="<td><a href=delQuestion?qid=>"+str(i+1)+"</td>"
		v+="<td align=center>"+ca+"</td>"
		v+="<td align=center>"+ua+"</td>"
	
		if ca==ua:
			v+="<td align=center>'correct'</td></tr>"
			corr=corr+1;
		else:
			v+="<td align=center>'In-correct'</td></tr>"
	v+="</table>"		
	today=date.today()
	dt=today.strftime("%Y-%m-%d")
	tm=today.strftime("%H-%M-%S")
	qr=quizresults(quizdate=dt,quiztime=tm,userid=eid,instname=inm,totalquestions=len(qs),correctanswer=corr)
	qr.save()
	
	
	v+="your result is "+str(corr)+"out of "+str(len(qs))
	resp=HttpResponse(v)
	return(resp)
def addinstructor(request):
	return render(request,'instructor.html')

def instructorSave(request):
	userid=request.POST["userid"]
	password=request.POST["password"]
	cpwd=request.POST["cpwd"]
	instname=request.POST["instname"]
	gen=request.POST["gender"]
	name=request.POST["name"]
	dob=request.POST["birthdate"]
	u=teacher(userid=userid,password=password,instname=instname,gender=gen,birthdate=dob,name=name)
	u.save()
	a="<h1>Record Saved </h1>"
	resp=HttpResponse(a)
	return(resp)
def instructorLogin(request):
	return render(request,'instructorLogin.html')
def instructorLoginCheck(request):
	userid=request.POST["userid"]
	password=request.POST["password"]
	qs=teacher.objects.filter(userid=userid,password=password)
	if qs:
		request.session['userid']=userid
		request.session['password']=password
		return render(request,"instructorHome.html",{"uname":qs[0].name})
	else:
		msg="<h1>Invalid User ID or Password </h1>"
		resp=HttpResponse(msg)
		return(resp)