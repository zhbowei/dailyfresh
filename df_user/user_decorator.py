#__author:  bwzhang
#__date:    2018/7/24
from django.http import HttpResponseRedirect


def login(fun):
    def login_fun(req,*args,**kwargs):
        if req.session.has_key('user_id'):
            return fun(req,*args,**kwargs)
        else:
            red = HttpResponseRedirect('/user/login/')
            red.set_cookie('url',req.get_full_path())
            return red
    return  login_fun