# -*- coding: utf-8 -*
from django.shortcuts import render

# Create your views here.

from django.shortcuts import render,render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from django.template import RequestContext
from django import forms
from backend.models import  User

'''class UserForm(forms.Form):
	username = forms.CharField(Label = '帳號', max_length=50)
	password = forms.CharField(Label = '密碼', max_length=50)
	name = forms.CharField(label = '姓名', max_length=50)
	pubname = forms.CharField(label = '暱稱', max_length=50)
	phone = forms.CharField(Label = '電話', max_length=50)
	email = forms.EmailField(Label = '電子信箱', max_length=200)'''

def HomePage(req):
	return render_to_response('HomePage.html' ,{})

def SignUp(req):
	return render_to_response('SignUp.html' ,{})

def Login(req):
	return render_to_response('Login.html' ,{})

def FindPet(req):
	return render_to_response('FindPet.html' ,{})

def FindMaster(req):
	return render_to_response('FindMaster.html' ,{})

def ChangeAccount(req):
	return render_to_response('ChangeAccount.html' ,{})

def ChangePassword(req):
	return render_to_response('ChangePassword.html' ,{})


#註冊
'''def SignUp(req):
	if req.method == 'POST':
		uf = UserForm(req.POST)
		if uf.is_valid():
			#获得表单数据
			username = uf.cleaned_data['username']
			password = uf.cleaned_data['password']
			name = uf.cleaned_data['name']
			pubname = uf.cleaned_data['pubname']
			phone = uf.cleaned_data['phone']
			email = uf.cleaned_data['email']
			#添加到数据库
			User.objects.create(username= username, password=password, name = name, pubname = pubname, phone = phone, email = email)
			return HttpResponse('regist success!!')
		else:
			uf = UserForm()
		return render_to_response('SignUp.html',{'uf':uf}, )'''
