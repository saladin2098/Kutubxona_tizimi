from django.db import models

from django.db import models

class Speciality(models.Model):
    name = models.CharField(max_length=30)
    code = models.IntegerField()
    start_date = models.DateField(null=True)
    is_active = models.CharField(max_length=15)
    def __str__(self):
        return self.name

class Teacher(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    degree =  models.CharField(max_length=20)
    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Subject(models.Model):
    name = models.CharField(max_length=30)
    speciality = models.ForeignKey(Speciality ,on_delete=models.SET_NULL, null=True )
    teachers = models.ManyToManyField(Teacher , null=True )
    def __str__(self):
        return self.name

