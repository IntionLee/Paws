from django.conf.urls import url,include
from django.contrib import admin
from backend import views

urlpatterns = [
    url(r'^HomePage/$', views.HomePage, name='HomePage'),
    url(r'^SignUp/$',views.SignUp,name = 'SignUp'),
    url(r'^Login/$',views.Login,name = 'Login'),
    url(r'^FindPet/$',views.FindPet,name = 'FindPet'),
    url(r'^FindMaster/$',views.FindMaster,name = 'FindMaster'),
    url(r'^ChangeAccount/$',views.ChangeAccount,name = 'ChangeAccount'),
    url(r'^ChangePassword/$',views.ChangePassword,name = 'ChangePassword'),
]