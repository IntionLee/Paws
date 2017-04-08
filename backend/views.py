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
from django.core.mail import send_mail
import random, string
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
		email=req.POST.get('email', '')

		if password != password2:
			state = 'repeat_error'
		else:
			if User.objects.filter(username = username):
				state = 'user_exist'
			elif User.objects.filter(email = email):
				state = 'email_exist'
			else:
				new_user = User.objects.create_user(username=username, password=password, email=email)
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
		petid = ''
		petcolor = ''
		petgender = ''
		size = ''
		ligation = ''
		petfeature = ''
		location = ''
		contactname = ''
		phonenumber = ''
		email = ''
		if req.method == 'POST':
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

			if req.POST.get('animal', '') == u'其他動物':
				if req.POST.get('animal2', '') == '' or req.POST.get('pettype2', '') == '':
					state = 'warn1'
			elif req.POST.get('pettype', '') == u'其他' and req.POST.get('pettype2', '') == '':
				state = 'warn2'
			elif req.POST.get('time', '') == '':
				state = 'warn0'
			else:
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
				new_lost_notice = MyLostNotice(flag=flag, poster=user, petimg=petimg, animal=animal, pettype=pettype, petid=petid, petcolor=petcolor, petgender=petgender, size=size
					, ligation=ligation, petfeature=petfeature, location=location, time=time, contactname=contactname, phonenumber=phonenumber, email=email)
				new_lost_notice.save()
				state = 'success'
	else:
		return HttpResponseRedirect(reverse('HomePage'))
	content = {
		'petid':petid,
		'petcolor':petcolor,
		'petgender':petgender,
		'size':size,
		'ligation':ligation,
		'petfeature':petfeature,
		'location':location,
		'contactname':contactname,
		'phonenumber':phonenumber,
		'email':email,
		'state': state,
		'user': user
	}
	return render(req, 'FindPet.html', content)

def FindMaster(req):
	if req.user.is_authenticated():
		user = req.user
		state = None
		petid = ''
		petcolor = ''
		petgender = ''
		size = ''
		ligation = ''
		petfeature = ''
		location = ''
		contactname = ''
		phonenumber = ''
		email = ''
		if req.method == 'POST':
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
			print(petfeature)

			if req.POST.get('animal', '') == u'其他動物':
				if req.POST.get('animal2', '') == '' or req.POST.get('pettype2', '') == '':
					state = 'warn1'
			elif req.POST.get('pettype', '') == u'其他' and req.POST.get('pettype2', '') == '':
				state = 'warn2'
			elif req.POST.get('time', '') == '':
				state = 'warn0'
			else:
				if req.POST.get('animal', '') == u'其他動物':
					animal = req.POST.get('animal', '')+'-'+req.POST.get('animal2', '')
					pettype = req.POST.get('pettype', '')+'-'+req.POST.get('pettype2', '')
				elif req.POST.get('pettype', '') == u'其他':
					animal = req.POST.get('animal', '')
					pettype = req.POST.get('pettype', '')+'-'+req.POST.get('pettype2', '')
				else:
					animal = req.POST.get('animal', '')
					pettype = req.POST.get('pettype', '')
				flag = 2
				new_lost_notice = MyLostNotice(flag=flag, poster=user, petimg=petimg, animal=animal, pettype=pettype, petid=petid, petcolor=petcolor, petgender=petgender, size=size
					, ligation=ligation, petfeature=petfeature, location=location, time=time, contactname=contactname, phonenumber=phonenumber, email=email)
				new_lost_notice.save()
				state = 'success'
	else:
		return HttpResponseRedirect(reverse('HomePage'))
	content = {
		'petid':petid,
		'petcolor':petcolor,
		'petgender':petgender,
		'size':size,
		'ligation':ligation,
		'petfeature':petfeature,
		'location':location,
		'contactname':contactname,
		'phonenumber':phonenumber,
		'email':email,
		'state': state,
		'user': user
	}
	return render(req, 'FindMaster.html', content)

def FindPetPost(req):
	if req.user.is_authenticated():
		user = req.user
	else:
		user = None

	state = None
	animal_list = MyLostNotice.objects.values_list('animal', flat=True).distinct()
	query_animal = req.GET.get('animal')

	if query_animal == 'all' or (not query_animal):
		postlist = MyLostNotice.objects.filter(flag=1).order_by('-time')
	elif query_animal == u'其他動物':
		postlist = MyLostNotice.objects.filter(flag=1, animal__contains=query_animal).order_by('-time')
	else:
		postlist = MyLostNotice.objects.filter(flag=1, animal=query_animal).order_by('-time')

	paginator = Paginator(postlist, 5)
	page = req.GET.get('page')
	try:
		postlist = paginator.page(page)
	except PageNotAnInteger:
		postlist = paginator.page(1)
	except EmptyPage:
		postlist = paginator.page(paginator.num_pages)

	content = {
		'user': user,
		'postlist': postlist,
		'animal_list': animal_list,
		'query_animal': query_animal,
	}
	return render(req, 'FindPetPost.html', content)

def FindMasterPost(req):
	if req.user.is_authenticated():
		user = req.user
	else:
		user = None
	animal_list = MyLostNotice.objects.values_list('animal', flat=True).distinct()
	query_animal = req.GET.get('animal')

	if query_animal == 'all' or (not query_animal):
		postlist = MyLostNotice.objects.filter(flag=2).order_by('-time')
	elif query_animal == u'其他動物':
		postlist = MyLostNotice.objects.filter(flag=2, animal__contains=query_animal).order_by('-time')
	else:
		postlist = MyLostNotice.objects.filter(flag=2, animal=query_animal).order_by('-time')

	paginator = Paginator(postlist, 5)
	page = req.GET.get('page')
	try:
		postlist = paginator.page(page)
	except PageNotAnInteger:
		postlist = paginator.page(1)
	except EmptyPage:
		postlist = paginator.page(paginator.num_pages)

	content = {
		'user': user,
		'postlist': postlist,
		'animal_list': animal_list,
		'query_animal': query_animal,
	}
	return render(req, 'FindMasterPost.html', content)

def Detail(req):
	if req.user.is_authenticated():
		user = req.user
	else:
		user = None
	mylostnotice_id = req.GET.get('id', '')
	if mylostnotice_id == '':
		return HttpResponseRedirect(reverse('HomePage'))
	try:
		mylostnotice = MyLostNotice.objects.get(pk=mylostnotice_id)
	except MyLostNotice.DoesNotExist:
		return HttpResponseRedirect(reverse('HomePage'))
	content = {
		'user': user,
		'mylostnotice': mylostnotice,
	}
	return render(req, 'Detail.html', content)

def Serch(req):
	if req.user.is_authenticated():
		user = req.user
	else:
		user = None
	flag = req.POST.get('flag', '')
	animal = req.POST.get('animal', '')
	pettype = req.POST.get('pettype', '')
	petid = req.POST.get('petid', '')
	petgender = req.POST.get('petgender', '')
	size = req.POST.get('size', '')
	ligation = req.POST.get('ligation', '')
	location = req.POST.get('location', '')
	postlist = MyLostNotice.objects.filter(flag__contains=flag, animal__contains=animal, pettype__contains=pettype, petid__contains=petid,
		petgender__contains=petgender, size__contains=size, ligation__contains=ligation, location__contains=location).order_by('-time')

	paginator = Paginator(postlist, 5)
	page = req.GET.get('page')
	try:
		postlist = paginator.page(page)
	except PageNotAnInteger:
		postlist = paginator.page(1)
	except EmptyPage:
		postlist = paginator.page(paginator.num_pages)
	content = {
		'user': user,
		'postlist': postlist,
		'flag': flag,
		'animal': animal,
		'pettype': pettype,
		'petid': petid,
		'petgender': petgender,
		'size': size,
		'ligation': ligation,
		'location': location,
	}
	return render(req, 'Serch.html', content)

def MyPost(req):
	if req.user.is_authenticated():
		user = req.user
		postlist = MyLostNotice.objects.filter(poster=user).order_by('-time')

	else:
		return HttpResponseRedirect(reverse('HomePage'))
	paginator = Paginator(postlist, 5)
	page = req.GET.get('page')
	try:
		postlist = paginator.page(page)
	except PageNotAnInteger:
		postlist = paginator.page(1)
	except EmptyPage:
		postlist = paginator.page(paginator.num_pages)
	content = {
		'user': user,
		'postlist': postlist,
	}
	return render(req, 'MyPost.html', content)

def ChangePost(req):
	if req.user.is_authenticated():
		state = None
		user = req.user
		mylostnotice_id = req.GET.get('id', '')
		if mylostnotice_id == '':
			return HttpResponseRedirect(reverse('HomePage'))
		try:
			mylostnotice = MyLostNotice.objects.get(pk=mylostnotice_id)
		except MyLostNotice.DoesNotExist:
			return HttpResponseRedirect(reverse('HomePage'))
		if req.method == 'POST':
			if mylostnotice.poster == user:
				mylostnotice.petid = req.POST.get('petid', '')
				mylostnotice.petcolor = req.POST.get('petcolor', '')
				mylostnotice.petgender = req.POST.get('petgender', '')
				mylostnotice.size = req.POST.get('size', '')
				mylostnotice.ligation = req.POST.get('ligation', '')
				mylostnotice.petfeature = req.POST.get('petfeature', '')
				mylostnotice.location = req.POST.get('location', '')
				mylostnotice.contactname = req.POST.get('contactname', '')
				mylostnotice.phonenumber = req.POST.get('phonenumber', '')
				mylostnotice.email = req.POST.get('email', '')
				mylostnotice.save()
				state = 'success'
			else:
				mylostnotice = None
				return HttpResponseRedirect(reverse('HomePage'))
		

	else:
		return HttpResponseRedirect(reverse('HomePage'))
	content = {
		'state': state,
		'user': user,
		'mylostnotice': mylostnotice,
	}
	return render(req, 'ChangePost.html', content)

def ForgetPassword(req):
	if req.user.is_authenticated():
		user = req.user
		return HttpResponseRedirect(reverse('HomePage'))
	user = None
	state = None
	if req.method == 'POST':
		email = req.POST.get('email', '')
		if email == '':
			state ='not_exist'
		try:
			myuser = User.objects.get(email=email)
			length = 16
			random_str = ''.join([random.choice(string.ascii_letters) for i in range(length)])
			myuser.set_password(random_str)
			myuser.save()
			send_mail(u'Paws-帳號/密碼找回', u'帳號：'+myuser.username+'\n'+u'密碼：'+random_str, 'paws_forget_password@foxmail.com', [email], fail_silently=False)
			state = 'success'
		except User.DoesNotExist:
			state ='not_exist'
	content = {
		'user': user,
		'state': state,
	}
	return render(req, 'ForgetPassword.html', content)


def DeletePost(req):
	if req.user.is_authenticated():
		mylostnotice_id = req.GET.get('id', '')
		if mylostnotice_id == '':
			return HttpResponseRedirect(reverse('HomePage'))
		try:
			MyLostNotice.objects.get(pk=mylostnotice_id).delete()
			return HttpResponseRedirect(reverse('MyPost'))
		except MyLostNotice.DoesNotExist:
			return HttpResponseRedirect(reverse('HomePage'))
	else:
		return HttpResponseRedirect(reverse('HomePage'))


#def DeleteAllPost(req):
#	MyLostNotice.objects.all().delete() 
#	return HttpResponseRedirect(reverse('HomePage'))
