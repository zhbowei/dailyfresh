from django.db import models
from tinymce.models import HTMLField
# Create your models here.


class TypeInfo(models.Model):
    title = models.CharField(max_length=20)
    isDelete = models.BooleanField(default=False)
    def __str__(self):
        return self.title
    class Meta:
        verbose_name = '分类信息'
        verbose_name_plural = '分类信息'

class GoodsInfo(models.Model):
    gtitle = models.CharField(max_length=20)
    gpic = models.ImageField(upload_to='df_goods')
    gprice = models.DecimalField(max_digits=5,decimal_places=2)
    isDelete = models.BooleanField(default=False)
    gunit = models.CharField(max_length=20,default='500g')
    gclick = models.IntegerField()
    gjianjie = models.CharField(max_length=200)
    gkucun = models.IntegerField()
    gcontext = HTMLField()
    gtype = models.ForeignKey(TypeInfo,on_delete=models.CASCADE)
    class Meta:
        verbose_name = '商品信息'
        verbose_name_plural = '商品信息'

