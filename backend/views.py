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
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from backend.models import  MyUser
from backend.models import  MyLostNotice

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
		if req.method == 'POST':
			if req.POST.get('animal', '') == u'其他動物':
				animal = req.POST.get('animal', '')+'-'+req.POST.get('animal2', '')
				pettype = req.POST.get('pettype', '')+'-'+req.POST.get('pettype2', '')
			elif req.POST.get('pettype', '') == u'其他':
				animal = req.POST.get('animal', '')
				pettype = req.POST.get('pettype', '')+'-'+req.POST.get('pettype2', '')
			else:
				animal = req.POST.get('animal', '')
				pettype = req.POST.get('pettype', '')
			flag = 1
			petimg = req.FILES.get('petimg')
			petid = req.POST.get('petid', '')
			petcolor = req.POST.get('petcolor', '')
			petgender = req.POST.get('petgender', '')
			size = req.POST.get('size', '')
			ligation = req.POST.get('ligation', '')
			petfeature = req.POST.get('petfeature', '')
			location = req.POST.get('location', '')
			time = req.POST.get('time', '')
			contactname = req.POST.get('contactname', '')
			phonenumber = req.POST.get('phonenumber', '')
			email = req.POST.get('email', '')

			new_lost_notice = MyLostNotice(flag=flag, petimg=petimg, animal=animal, pettype=pettype, petid=petid, petcolor=petcolor, petgender=petgender, size=size
				, ligation=ligation, petfeature=petfeature, location=location, time=time, contactname=contactname, phonenumber=phonenumber, email=email)
			new_lost_notice.save()
			state = 'success'
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
		if req.method == 'POST':
			if req.POST.get('animal', '') == u'其他動物':
				animal = req.POST.get('animal', '')+'-'+req.POST.get('animal2', '')
				pettype = req.POST.get('pettype', '')+'-'+req.POST.get('pettype2', '')
			elif req.POST.get('pettype', '') == u'其他':
				animal = req.POST.get('animal', '')
				pettype = req.POST.get('pettype', '')+'-'+req.POST.get('pettype2', '')
			else:
				animal = req.POST.get('animal', '')
				pettype = req.POST.get('pettype', '')
			flag = 1
			petimg = req.FILES.get('petimg')
			petid = req.POST.get('petid', '')
			petcolor = req.POST.get('petcolor', '')
			petgender = req.POST.get('petgender', '')
			size = req.POST.get('size', '')
			ligation = req.POST.get('ligation', '')
			petfeature = req.POST.get('petfeature', '')
			location = req.POST.get('location', '')
			time = req.POST.get('time', '')
			contactname = req.POST.get('contactname', '')
			phonenumber = req.POST.get('phonenumber', '')
			email = req.POST.get('email', '')

			new_lost_notice = MyLostNotice(flag=flag, petimg=petimg, animal=animal, pettype=pettype, petid=petid, petcolor=petcolor, petgender=petgender, size=size
				, ligation=ligation, petfeature=petfeature, location=location, time=time, contactname=contactname, phonenumber=phonenumber, email=email)
			new_lost_notice.save()
			state = 'success'
	else:
		return HttpResponseRedirect(reverse('HomePage'))
	content = {
		'state': state,
		'user': user
	}
	return render(req, 'FindMaster.html', content)

def ListAllPost(req):
	if req.user.is_authenticated():
		user = req.user
		state = None
		postlist = MyLostNotice.objects.all()
		paginator = Paginator(postlist, 5)
		page = req.GET.get('page')
		try:
			postlist = paginator.page(page)
		except PageNotAnInteger:
			postlist = paginator.page(1)
		except EmptyPage:
			postlist = paginator.page(paginator.num_pages)
	else:
		return HttpResponseRedirect(reverse('HomePage'))
	content = {
		'user': user,
		'postlist': postlist,
	}
	return render(req, 'ListAllPost.html', content)

def DeleteAllPost(req):
	MyLostNotice.objects.all().delete() 
	return HttpResponseRedirect(reverse('HomePage'))
