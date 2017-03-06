# -*- coding: utf-8 -*
from django.shortcuts import render

# Create your views here.

from django.shortcuts import render,render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.decorators import user_passes_test, login_required
from django.contrib.auth.models import User
from django.contrib import auth
from django.template import RequestContext
from django.core.urlresolvers import reverse
from django import forms
from backend.models import  MyUser

def HomePage(req):
	user = req.user if req.user.is_authenticated() else None
	content = {
        'user': user,
    }
	return render(req, 'HomePage.html', content)

def SignUp(req):
	if req.user.is_authenticated():
		return HttpResponseRedirect(reverse('HomePage'))
	state = None
	if req.method == 'POST':
		username = req.POST.get('username', '')
		password = req.POST.get('password', '')
		password2 = req.POST.get('password2', '')

		if password != password2:
			state = 'repeat_error'
		else:
			if User.objects.filter(username = username):
				state = 'user_exist'
			else:
				new_user = User.objects.create_user(username=username, password=password, email=req.POST.get('email', ''))
				new_user.save()
				new_my_user = MyUser(user=new_user, name=req.POST.get('name', ''), pubname=req.POST.get('pubname', ''), phone=req.POST.get('phone', ''))
				new_my_user.save()
				state = 'success'
	content = {
	    'state': state,
	    'user': None
	}
	return render(req, 'SignUp.html', content)

def Login(req):
	if req.user.is_authenticated():
		return HttpResponseRedirect(reverse('HomePage'))
	state = None
	if req.method == 'POST':
		username = req.POST.get('username', '')
		password = req.POST.get('password', '')
		user = auth.authenticate(username=username, password=password)
		if user is not None:
			auth.login(req, user)
			return HttpResponseRedirect(reverse('HomePage'))
		else:
			state = 'not_exist_or_password_error'
	content = {
		'state': state,
		'user': None
	}
	return render(req, 'Login.html', content)

def Logout(req):
	auth.logout(req)
	return HttpResponseRedirect(reverse('HomePage'))

def ChangeAccount(req):
	if req.user.is_authenticated():
		user = req.user
		state = None
		if req.method == 'POST':
			name = req.POST.get('name', '')
			pubname = req.POST.get('pubname', '')
			phone = req.POST.get('phone', '')
			myuser = MyUser.objects.get(user = user)
			if name != "":
				myuser.name = name
				myuser.save()
			elif pubname != "":
				myuser.pubname = pubname
				myuser.save()
			elif phone != "":
				myuser.phone = phone
				myuser.save()
			state = 'success'
	else:
		return HttpResponseRedirect(reverse('HomePage'))
	content = {
		'state': state,
		'user': user
	}
	return render(req, 'ChangeAccount.html', content)

def ChangePassword(req):
	if req.user.is_authenticated():
		user = req.user
		state = None
		if req.method == 'POST':
			password = req.POST.get('password', '')
			newpassword = req.POST.get('newpassword', '')
			newpassword2 = req.POST.get('newpassword2', '')
			if user.check_password(password):
				if newpassword != newpassword2:
					state = 'repeat_error'
				else:
					user.set_password(newpassword)
					user.save()
					state = 'success'
			else:
				state = 'password_error'
	else:
		return HttpResponseRedirect(reverse('HomePage'))
	content = {
		'state': state,
		'user': user
	}
	return render(req, 'ChangePassword.html', content)

def FindPet(req):
	if req.user.is_authenticated():
		user = req.user
		state = None
	else:
		return HttpResponseRedirect(reverse('HomePage'))
	content = {
		'state': state,
		'user': user
	}
	return render(req, 'FindPet.html', content)

def FindMaster(req):
	if req.user.is_authenticated():
		user = req.user
		state = None
	else:
		return HttpResponseRedirect(reverse('HomePage'))
	content = {
		'state': state,
		'user': user
	}
	return render(req, 'FindMaster.html', content)