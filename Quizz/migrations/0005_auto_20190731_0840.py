# Generated by Django 2.2.3 on 2019-07-31 03:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Quizz', '0004_quizresult'),
    ]

    operations = [
        migrations.CreateModel(
            name='quizresults',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quizid', models.CharField(max_length=50)),
                ('quizdate', models.DateField()),
                ('quiztime', models.CharField(max_length=45)),
                ('userid', models.CharField(max_length=50)),
                ('instname', models.CharField(max_length=50)),
                ('totalquestions', models.CharField(max_length=50)),
                ('correctanswer', models.CharField(max_length=50)),
            ],
        ),
        migrations.DeleteModel(
            name='quizresult',
        ),
    ]
