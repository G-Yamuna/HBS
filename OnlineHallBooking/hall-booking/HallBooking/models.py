from django.db import models
from django.contrib.auth.models import AbstractUser
from django.dispatch import receiver

# Create your models here.

class User(AbstractUser):
	g = [('M','Male'),('F','Female'),('O','Others')]
	gender = models.CharField(max_length=10,choices=g)
	age = models.IntegerField(default=18)
	mobile_no = models.CharField(max_length=10)
	dob = models.DateField(null=True)
	pid_no=models.CharField(max_length=10) 
	address_line1=models.CharField(max_length=200)
	address_line2=models.CharField(max_length=200)
	city=models.CharField(max_length=30)
	state=models.CharField(max_length=30)
	country=models.CharField(max_length=30)
	profile = models.ImageField(upload_to='Profile_pics/',default='avatar.png')
	r = [(0,'guest'),(1,'user'),(2,'manager')]
	role = models.IntegerField(choices=r,default=0)

# @receiver(post_save,sender=User)
# def CrtPfle(sender,instance,created,**kwargs):
# 	 if created: 
# 	 	Updf.objects.create(pr=instance)

class RoleRqst(models.Model):
	t=[(1,'user'),(2,'manager')]
	uname= models.CharField(max_length=30)
	roletype = models.PositiveIntegerField(choices=t)
	proof = models.ImageField(blank=True)
	is_checked=models.BooleanField(default=0)
	uid= models.OneToOneField(User,on_delete=models.CASCADE)

class AdHl(models.Model):
	# t=[('Marriage',"MarriageHall"),('Seminar',"SeminarHall"),('Event',"EventHall")]
	name = models.CharField(max_length=100)
	address = models.CharField(max_length=100)
	landmark = models.CharField(max_length=50)
	h = [(1,'Marriage'),(2,'Seminar'),(3,'Event')]
	halltype = models.IntegerField(choices=h)
	aircond = models.CharField(max_length=10)
	occupancy = models.IntegerField(null=True)
	area = models.CharField(max_length=20)
	fil = models.FileField(upload_to="Hall_Images/")
	add = models.ForeignKey(User,on_delete=models.CASCADE)
	





