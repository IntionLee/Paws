from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class MyUser(models.Model):
	user = models.OneToOneField(User)
	name = models.CharField(max_length=50)
	pubname = models.CharField(max_length=50)
	phone = models.CharField(max_length=50)
	email = models.EmailField(max_length=100)

	def __unicode__(self):
		return self.user.username
