from django.db import models

# Create your models here.


class School(models.Model):
    Id = models.AutoField(primary_key = True)
    Name = models.CharField(max_length=200)
    Create_at = models.DateTimeField(auto_now=True)
    Update_at = models.DateTimeField(null=True)
    
class Student(models.Model):
    Id = models.AutoField(primary_key = True)
    Name = models.CharField(max_length=200)
    Enrollment = models.CharField(unique=True,max_length=200)
    School = models.ForeignKey(School, on_delete=models.CASCADE)
    Create_at = models.DateTimeField(auto_now=True)
    Update_at = models.DateTimeField(null=True)