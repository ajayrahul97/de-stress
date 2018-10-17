# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import hashlib

# Create your models here.

class User(models.Model):
	password = models.CharField(max_length=100)
	name = models.CharField(max_length=200)
	address = models.TextField()
	email = models.EmailField(primary_key = True)
	blood_group = models.CharField(max_length=3)
	diseases = models.CharField(max_length=200)
	def __str__(self):
		return str(self.email)
	def make_password(self ,password):
		assert password
		hashedpassword = hashlib.md5(password).hexdigest()
		return hashedpassword
	def check_password(self, password):
		assert password
		hashed = hashlib.md5(password).hexdigest()
		return self.password == hashed
	def set_password(self, password):
		self.password = password


class Map(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	latitude = models.FloatField()
	longitude = models.FloatField()
	name = models.CharField(max_length=200)
	def __str__(self):
		return str(self.id)