from django.conf.urls import url,include
from django.contrib import admin
from backend import views

urlpatterns = [
    url(r'^HomePage/$', views.HomePage, name='HomePage'),
    url(r'^SignUp/$',views.SignUp,name = 'SignUp'),
    url(r'^Login/$',views.Login,name = 'Login'),
    url(r'^Logout/$', views.Logout, name='Logout'),
    url(r'^FindPet/$',views.FindPet,name = 'FindPet'),
    url(r'^FindMaster/$',views.FindMaster,name = 'FindMaster'),
    url(r'^ChangeAccount/$',views.ChangeAccount,name = 'ChangeAccount'),
    url(r'^ChangePassword/$',views.ChangePassword,name = 'ChangePassword'),
    url(r'^FindPetPost/$', views.FindPetPost, name= 'FindPetPost'),
    url(r'^FindMasterPost/$', views.FindMasterPost, name= 'FindMasterPost'),
    url(r'^DeleteAllPost/$', views.DeleteAllPost, name= 'DeleteAllPost'),
]