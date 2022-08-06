from django.db import models

# Create your models here.

class user(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)

class grade(models.Model):
    name = models.ForeignKey(user , on_delete = models.CASCADE)
    course = models.CharField(max_length=6)
    marks = models.FloatField()
    cgpa = models.FloatField()