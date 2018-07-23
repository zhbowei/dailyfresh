from django.contrib import admin
from .models import TypeInfo,GoodsInfo
# Register your models here.
class TypeInfoAdmin(admin.ModelAdmin):
    list_display = ['id','title']
class GoodsInfoAdmin(admin.ModelAdmin):
    list_per_page = 15
    list_display = ['id','gtitle','gprice','gunit','gclick','gkucun','gcontext','gtype']
admin.site.register(TypeInfo,TypeInfoAdmin)
admin.site.register(GoodsInfo,GoodsInfoAdmin)
