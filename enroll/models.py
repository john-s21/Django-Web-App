from django.db import models
from django.urls import reverse
# from django.utils import timezone
from datetime import datetime


class Data(models.Model):

    ATT = (
        ('Student Attendance', (
            (u'YES', u'Y'),
            (u'NO', u'N'),
        )),
    )
    DAY = (
        ('Choose your session', (
            (u'SATURDAY', u'saturday'),
            (u'SUNDAY', u'sunday'),
        )),
    )
    COURSE = (
        ('Select your course', (
            (u'PYTHON', u'python'),
            (u'DOT_NET', u'.net'),
            (u'C', u'c'),
            (u'C++', u'c++'),
            (u'PHP', u'php'),
            (u'XML', u'xml'),
        )),
    )

    id = models.AutoField(auto_created=True, primary_key=True)
    name = models.CharField(max_length=15, null=False, unique=True)
    course = models.CharField(max_length=10, blank=False, null=False, choices=COURSE)
    session = models.CharField(max_length=8, blank=False, null=False, choices=DAY)
    attendance = models.CharField(max_length=3, blank=False, null=False, choices=ATT)
    date = models.DateTimeField(default=datetime.now, editable=True)
    amount = models.IntegerField(blank=False, null=False)
    img = models.ImageField(upload_to='images/', default="")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('records', args=[str(self.id)])


class Reg(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True)
    usr_name = models.CharField(max_length=15, unique=True, null=False, blank=False)
    pwd = models.CharField(max_length=15, null=False, blank=False, unique=True)
    mail = models.EmailField(unique=True, null=False, blank=False)

    def __str__(self):
        return self.usr_name
