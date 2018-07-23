from django.http import JsonResponse, HttpResponseRedirect
from django.shortcuts import render,redirect
from .models import *
from hashlib import sha1
# Create your views here.

def register(req):
    return render(req,'df_user/register.html')
def register_handle(req):
    #1.获取前端传入的值
    uname = req.POST.get('user_name')
    upwd = req.POST.get('pwd')
    upwd2 = req.POST.get('cpwd')
    uemail = req.POST.get('email')
    #判断两次密码输入是否一致
    if upwd !=upwd2:
        return redirect('/user/register/')
    #密码加密
    s1 = sha1()
    s1.update(upwd2.encode("utf8"))
    upwd3 = s1.hexdigest()
    #数值记录在数据库中
    user = UserInfo()
    user.uname = uname
    user.upwd = upwd3
    user.uemail = uemail
    user.save()
    return redirect('/user/login/')
def register_exit(req):
    uname = req.GET.get('uname')
    count = UserInfo.objects.filter(uname=uname).count()
    print(count)
    return JsonResponse({"count":count})
def login(req):
    uname = req.COOKIES.get('uname')
    context = {'title':'用户登录','error_name':0,'error_pwd':'0','uname':uname}
    return render(req,'df_user/login.html',context)
def login_headle(req):
    #接受请求信息
    uname = req.POST.get('username')
    upwd = req.POST.get('pwd')
    jizhu = req.POST.get('jizhu',0)
    #根据用户名查询对象
    users = UserInfo.objects.filter(uname=uname)
    # print(users)
    if len(users) == 1:
        s1 = sha1()
        s1.update(upwd.encode("utf8"))
        jupwd = s1.hexdigest()
        #如果密码正确，则转到用户中心
        if jupwd == users[0].upwd:
            red = HttpResponseRedirect('/user/info/')
            if jizhu != 0:
                red.set_cookie('uname',uname)
            else:
                red.set_cookie('uname','',max_age=1)
            req.session['user_id'] = users[0].id
            req.session['user_name'] = uname
            return red
        else:
            context = {'title': '用户登录', 'error_name':0, 'error_pwd':1, 'uname': uname,'upwd':upwd}
            return render(req,'df_user/login.html',context)
    context = {'title': '用户登录','error_name':1, 'error_pwd':0, 'uname': uname,'upwd':upwd}
    return render(req,'df_user/login.html',context)
def info(req):
    user_email = UserInfo.objects.get(id=req.session['user_id']).uemail
    centext = {'title':'用户中心',
               'page_name': 1,
               'user_email':user_email,
               'user_name':req.session['user_name']
               }
    return render(req,'df_user/user_center_info.html',centext)
def order(req):
    centext = {'title':"用户中心",
               'page_name': 1,
               }
    return render(req,'df_user/user_center_order.html',centext)
def site(req):
    user = UserInfo.objects.get(id=req.session['user_id'])
    if req.method=="POST":
        user.ush = req.POST.get('ushou')
        user.uaddress = req.POST.get('uaddress')
        user.uyoubian = req.POST.get('uyoubian')
        user.uphone = req.POST.get('uphone')
        user.save()
    centext = {'title':'用户中心',
               'page_name': 1,
               'user':user,
    }
    return render(req,'df_user/user_center_site.html',centext)


