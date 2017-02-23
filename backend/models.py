from __future__ import unicode_literals

from django.db import models

# Create your models here.

class User(models.Model):
	username = models.CharField(max_length=50)
	password = models.CharField(max_length=50)
	name = models.CharField(max_length=50)
	pubname = models.CharField(max_length=50)
	phone = models.CharField(max_length=50)
	email = models.EmailField(max_length=100)

	def __unicode__(self):
		return self.username
