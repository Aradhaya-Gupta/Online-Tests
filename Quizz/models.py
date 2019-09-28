from django.db import models
class institute(models.Model):
	instname=models.CharField(max_length=50)
	userid=models.CharField(max_length=50,primary_key=True)
	insttype=models.CharField(max_length=50)
	address=models.CharField(max_length=50)
	city=models.CharField(max_length=50)
	contactno=models.CharField(max_length=50)
	password=models.CharField(max_length=50)


class student(models.Model):
	id=models.CharField(max_length=50,primary_key=True)
	studentname=models.CharField(max_length=50)
	gender=models.CharField(max_length=50)
	birthdate=models.DateField()
	userid=models.CharField(max_length=50)
	password=models.CharField(max_length=50)
	instname=models.CharField(max_length=50)
class teacher(models.Model):
	id=models.CharField(max_length=50,primary_key=True)
	name=models.CharField(max_length=50)
	gender=models.CharField(max_length=50)
	birthdate=models.DateField()
	userid=models.CharField(max_length=50)
	password=models.CharField(max_length=50)
	instname=models.CharField(max_length=50)
class quizset(models.Model):
	instname=models.CharField(max_length=50)
	gues=models.CharField(max_length=50)
	answer1=models.CharField(max_length=50)
	answer2=models.CharField(max_length=50)
	answer3=models.CharField(max_length=50)
	answer4=models.CharField(max_length=50)
	correctanswer=models.CharField(max_length=50)
class quizresults(models.Model):
	quizid=models.CharField(max_length=50)
	quizdate=models.DateField()
	quiztime=models.CharField(max_length=45) 
	userid=models.CharField(max_length=50)
	instname=models.CharField(max_length=50)
	totalquestions=models.CharField(max_length=50)
	correctanswer=models.CharField(max_length=50)