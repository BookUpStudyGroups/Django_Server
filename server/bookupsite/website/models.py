from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.contrib.postgres.fields import JSONField

from django.db import models


class Class(models.Model):
	department = models.CharField(max_length=4)
	number = models.IntegerField()
	period = models.CharField(max_length=3)
	prof = models.CharField(max_length=20)
	title = models.CharField(max_length=30)
	groups = models.ManyToManyField('Groups')

class UserBuddy(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	
	classes = models.ManyToManyField('Class')
	groups = models.ManyToManyField('Groups')
	buddies = models.ManyToManyField('StudyBuddy')
	
class Message(models.Model):
	message = models.CharField(max_length=256)
	date = models.DateField(auto_now_add=True)
	author = models.ForeignKey('UserBuddy', on_delete=models.CASCADE,)
	group = models.ForeignKey('Groups', on_delete=models.CASCADE,)
class StudyBuddy(models.Model):
	user1 = models.ForeignKey('UserBuddy', on_delete=models.CASCADE, related_name='user1')
	user2 = models.ForeignKey('UserBuddy', on_delete=models.CASCADE, related_name='user2')
	class1 = models.ForeignKey('Class', on_delete=models.CASCADE,)
	
	times = JSONField()
class Groups(models.Model):
	name = models.CharField(max_length=20)
	size = models.IntegerField()
	location = models.CharField(max_length=256)
	latitude = models.DecimalField(max_digits=7, decimal_places=6)
	longitude = models.DecimalField(max_digits=7, decimal_places=6)
	priv = models.BooleanField()
