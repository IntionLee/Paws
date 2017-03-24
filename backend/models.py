from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class MyUser(models.Model):
	user = models.OneToOneField(User)
	name = models.CharField(max_length=50)
	pubname = models.CharField(max_length=50)
	phone = models.CharField(max_length=50)

	def __unicode__(self):
		return self.user.username

class MyLostNotice(models.Model):
	flag = models.IntegerField(default=0)
	poster = models.ForeignKey(User)
	petimg = models.ImageField(upload_to='image')
	animal = models.CharField(max_length=50)
	pettype = models.CharField(max_length=50)
	petid = models.CharField(max_length=50)
	petcolor = models.CharField(max_length=50)
	petgender = models.CharField(max_length=50)
	size = models.CharField(max_length=50)
	ligation = models.CharField(max_length=50)
	petfeature = models.CharField(max_length=250)
	location = models.CharField(max_length=50)
	time = models.DateField(default=0)
	contactname = models.CharField(max_length=50)
	phonenumber = models.CharField(max_length=50)
	email = models.EmailField(max_length=100)

	class META:
 		ordering = ['-time']