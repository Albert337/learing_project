from __future__ import unicode_literals
from django.db import models

# Create your models here.
###类似于对表的描述
class cal(models.Model):
    value_a=models.CharField(max_length=10)
    value_b=models.FloatField(max_length=10)
    result=models.CharField(max_length=30)