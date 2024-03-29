# Generated by Django 2.2.3 on 2019-07-24 03:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Quizz', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='institute',
            fields=[
                ('instname', models.CharField(max_length=50)),
                ('userid', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('insttype', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('contactno', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='quiz',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quizid', models.CharField(max_length=50)),
                ('quizname', models.CharField(max_length=50)),
                ('gender', models.CharField(max_length=50)),
                ('birthdate', models.DateField()),
                ('userid', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
                ('instname', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='student',
            fields=[
                ('id', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('studentname', models.CharField(max_length=50)),
                ('gender', models.CharField(max_length=50)),
                ('birthdate', models.DateField()),
                ('userid', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
                ('instname', models.CharField(max_length=50)),
            ],
        ),
        migrations.DeleteModel(
            name='emails',
        ),
        migrations.DeleteModel(
            name='users',
        ),
    ]
