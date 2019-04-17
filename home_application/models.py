# -*- coding: utf-8 -*-
from django.db import models

class host(models.Model):
    when_created = models.DateTimeField(u"创建时间", null=True, auto_now_add=True)
    ip = models.CharField(u"ip",max_length=128)
    name = models.CharField(u"主机名称",max_length=128)
    system = models.CharField(u"系统",max_length=128)
    yun = models.CharField(u"云区域",max_length=128)
    yun_id = models.CharField(u"云id",max_length=128,default="")
    biz = models.CharField(u"业务",max_length=128)
    biz_id = models.CharField(u"业务id",max_length=128,default="")
    other = models.TextField(u"",default="其他")
    is_monitor = models.BooleanField(u"是否监控",default=False)

class FuZai(models.Model):
    when_created = models.DateTimeField(u"创建时间", null=True, auto_now_add=True)
    ip = models.CharField(u"",max_length=128)
    value = models.CharField(u"",max_length=128)

class HostData(models.Model):
    when_created = models.DateTimeField(u"创建时间", null=True, auto_now_add=True)
    ip = models.CharField(u"ip",max_length=128)
    biz_id = models.CharField(u"业务id",max_length=128,default="")
    yun_id = models.CharField(u"云id",max_length=128,default="")
    memory = models.CharField(u"内存",max_length=128)
    cpu = models.CharField(u"cpu",max_length=128)
    disk = models.CharField(u"磁盘",max_length=128)

