# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from .models import User, Map

# Create your views here.

def index(request):
    return HttpResponse("Hello, world. You're at the index.")

def users(request):
	userlist = User.objects.all()
	return HttpResponse(userlist)