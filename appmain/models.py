from __future__ import unicode_literals
from django.db import models

# Create your models here.

class SiteSetting(models.Model):

	sitename = models.CharField(max_length=150)
	fb 		= models.CharField(max_length=150)
	tw 		= models.CharField(max_length=150)
	ig 		= models.CharField(max_length=150)
	yt 		= models.CharField(max_length=150)
	phone 	= models.CharField(max_length=150)
	website 	= models.CharField(max_length=150)
	set_name = models.CharField(max_length=150)

	def __str__(self):
		return self.set_name + ' | ' + str(self.pk)