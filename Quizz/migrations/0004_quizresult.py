# Generated by Django 2.2.3 on 2019-07-30 04:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Quizz', '0003_auto_20190726_0912'),
    ]

    operations = [
        migrations.CreateModel(
            name='quizresult',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
    ]
