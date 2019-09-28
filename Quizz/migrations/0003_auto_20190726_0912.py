# Generated by Django 2.2.3 on 2019-07-26 03:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Quizz', '0002_auto_20190724_0859'),
    ]

    operations = [
        migrations.CreateModel(
            name='quizset',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('instname', models.CharField(max_length=50)),
                ('gues', models.CharField(max_length=50)),
                ('answer1', models.CharField(max_length=50)),
                ('answer2', models.CharField(max_length=50)),
                ('answer3', models.CharField(max_length=50)),
                ('answer4', models.CharField(max_length=50)),
                ('correctanswer', models.CharField(max_length=50)),
            ],
        ),
        migrations.DeleteModel(
            name='quiz',
        ),
    ]
