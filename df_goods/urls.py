#__author:  bwzhang
#__date:    2018/7/22
from django.conf.urls import url
from . import views
urlpatterns = [
    url('^$',views.index),
    url(r'^list(\d+)_(\d+)_(\d+)/$',views.list),
    url(r'^(\d+)/$',views.detail),
]