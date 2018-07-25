#__author:  bwzhang
#__date:    2018/7/24
from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$',views.cart,name='cart'),
    url(r'^add(\d+)_(\d+)/$',views.add),
    url(r'^edit(\d+)_(\d+)/$',views.edit),
    url(r'^delete(\d+)/$',views.delete),
    url(r'^place_order/$',views.place_order),
]