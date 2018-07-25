#coding=utf-8
#__author:  bwzhang
#__date:    2018/7/21
from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^register/$',views.register),
    url(r'^register_handle/$',views.register_handle),
    url(r'^register_exit/$', views.register_exit),
    url(r'^login/$', views.login),
    url(r'^login_headle/$',views.login_headle),
    url(r'^logout/$',views.logout),
    url(r'^info',views.info),
    url(r'^order',views.order),
    url(r'^site',views.site),
]