from django.db import models
from django.contrib.auth.models import AbstractUser
class User(AbstractUser):
    usertype=models.CharField(max_length=100)
class Department(models.Model):
    Dep_Name=models.CharField(max_length=100)
class Doctors(models.Model):
    Dep_id=models.ForeignKey(Department,on_delete=models.CASCADE)
    user_id=models.ForeignKey(User,on_delete=models.CASCADE)
    Phoneno=models.BigIntegerField()
    Qualifications=models.CharField(max_length=100)
    Address=models.CharField(max_length=200)
    def __str__(self):
        return f"{self.user_id.first_name} {self.user_id.last_name} - {self.Qualifications}"


    
    
class Patient(models.Model):
    user_id=models.ForeignKey(User,on_delete=models.CASCADE)
    #Dep_id=models.ForeignKey(Department,on_delete=models.CASCADE)
    Address=models.CharField(max_length=200)
    Phone=models.BigIntegerField()
    Age=models.PositiveIntegerField()
class Booking(models.Model):
    patient = models.ForeignKey(User, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctors, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    status = models.CharField(max_length=10, default='pending')

    





# Create your models here.
