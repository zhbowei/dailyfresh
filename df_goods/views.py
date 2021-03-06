from django.core.paginator import Paginator
from django.shortcuts import render
from .models import  *
# Create your views here.
def index(req):
    typelist = TypeInfo.objects.all()
    #查询各分类的最新4条，最热4条
    type0 = typelist[0].goodsinfo_set.order_by('-id')[0:4]
    type01 = typelist[0].goodsinfo_set.order_by('-gclick')[0:4]
    type1 = typelist[1].goodsinfo_set.order_by('-id')[0:4]
    type11 = typelist[1].goodsinfo_set.order_by('-gclick')[0:4]
    type2 = typelist[2].goodsinfo_set.order_by('-id')[0:4]
    type21 = typelist[2].goodsinfo_set.order_by('-gclick')[0:4]
    type3 = typelist[3].goodsinfo_set.order_by('-id')[0:4]
    type31 = typelist[3].goodsinfo_set.order_by('-gclick')[0:4]
    type4 = typelist[4].goodsinfo_set.order_by('-id')[0:4]
    type41 = typelist[4].goodsinfo_set.order_by('-gclick')[0:4]
    type5 = typelist[5].goodsinfo_set.order_by('-id')[0:4]
    type51 = typelist[5].goodsinfo_set.order_by('-gclick')[0:4]
    context = {
        'title':'首页',
        'page_name':0,
        'type0': type0, 'type01': type01,
        'type1': type1, 'type11': type11,
        'type2': type2, 'type21': type21,
        'type3': type3, 'type31': type31,
        'type4': type4, 'type41': type41,
        'type5': type5, 'type51': type51,
    }
    return render(req,'df_goods/index.html',context)
#tid为type的id，pindex为页数，sort为以什么进行分页
def list(req,tid,pindex,sort):
    typeinfo = TypeInfo.objects.get(id=int(tid))
    news = typeinfo.goodsinfo_set.order_by('-id')[0:2]
    if sort == '1':
        good_list = GoodsInfo.objects.filter(gtype_id=int(tid)).order_by('-id')
    elif sort == '2':
        good_list = GoodsInfo.objects.filter(gtype=int(tid)).order_by('-gprice')
    elif sort == '3':
        good_list = GoodsInfo.objects.filter(gtype_id=int(tid)).order_by('-gclick')
    paginator = Paginator(good_list,10)
    page = paginator.page(int(pindex))
    context = {
        'title':'列表',
        'page':page,
        'typeinfo':typeinfo,
        'news':news,
        'sort':sort,
        'paginator':paginator,
    }
    return render(req, 'df_goods/list.html',context)
def detail(req,id):
    goods = GoodsInfo.objects.get(pk=int(id))
    goods.gclick = goods.gclick+1
    goods.save()
    news = goods.gtype.goodsinfo_set.order_by('-id')[0:2]
    context = {
        'title':goods.gtype.title,
        'page_name': 0,
        'goods':goods,
        'news':news,
        'id':id,
    }
    return render(req,'df_goods/detail.html',context)
