from email.policy import default
from operator import mod
from django.db import models
from admins.models import Accounts
import uuid
# Create your models here.

class Employe(models.Model):
    designation = models.CharField(max_length = 25)
    employe_name = models.CharField(max_length = 30)
    employe_id = models.UUIDField(default=uuid.uuid4,null=True,blank=True)
    employe_created_date = models.DateField(auto_now_add=True)
    email = models.CharField(max_length=30,unique=True)
    mobile_number = models.CharField(max_length=15)
    total_leave = models.IntegerField(default=0)


class LeaveApplication(models.Model):
    Employe = models.ForeignKey(Employe, on_delete = models.CASCADE)
    leave_starting_date = models.DateField()
    leave_ending_date = models.DateField()
    leave_applying_date = models.DateField(auto_now_add=True)
    status = models.CharField(max_length = 15, default="pending")
    docfile = models.FileField(upload_to='documents/%Y/%m/%d')