# Generated by Django 3.1.4 on 2021-01-05 07:50

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=15, unique=True)),
                ('course', models.CharField(choices=[('Select your course', (('PYTHON', 'python'), ('DOT_NET', '.net'), ('C', 'c'), ('C++', 'c++'), ('PHP', 'php'), ('XML', 'xml')))], max_length=10)),
                ('session', models.CharField(choices=[('Choose your session', (('SATURDAY', 'saturday'), ('SUNDAY', 'sunday')))], max_length=8)),
                ('attendance', models.CharField(choices=[('Student Attendance', (('YES', 'Y'), ('NO', 'N')))], max_length=3)),
                ('date', models.DateTimeField(default=datetime.datetime.now)),
                ('amount', models.IntegerField()),
                ('img', models.ImageField(default='', upload_to='images/')),
            ],
        ),
    ]
