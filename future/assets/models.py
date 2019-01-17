# -*- coding:utf-8 -*-
# author: "Xianglei Kong"

from django.db import models

# Create your models here.

idc_operator = (
    (0, u"电信"),
    (1, u"联通"),
    (2, u"移动"),
    (3, u"铁通"),
    (4, u"混合"),
)
idc_type = (
    (0, u"CDN"),
    (1, u"业务")
)

class IDC(models.Model):
    name = models.CharField(max_length=64, verbose_name="机房名称")
    address = models.CharField(max_length=128, blank=True, null=True, verbose_name="机房地址")
    operator = models.IntegerField(verbose_name=u"运营商", choices=idc_operator, blank=True, null=True)
    type = models.IntegerField(verbose_name=u"机房类型", choices=idc_type, blank=True, null=True)
    comment = models.TextField(blank=True, null=True, verbose_name=u"备注")

    def __str__(self):
        return u'%s %s %d %d %s ' % (self.name, self.address, self.operator, self.type, self.comment)

    class Meta:
        verbose_name = u"IDC机房"
        verbose_name_plural = verbose_name
        app_label = 'assets'

use_type = (
    (0, "测试"),
    (1, "正式"),
    (2, "跨服")
)

class Project(models.Model):
    project_name = models.CharField(max_length=64, verbose_name="项目名称")
    aliases_name = models.CharField(max_length=64, verbose_name="项目简称", unique=True)
    business_name = models.CharField(max_length=64, verbose_name="业务名称")
    business_aliases_name = models.CharField(max_length=64, verbose_name="业务简称")
    use_name = models.IntegerField(verbose_name="业务用途", choices=use_type, blank=True, null=True)
    comment = models.TextField(blank=True, null=True, verbose_name=u"备注")

    def __str__(self):
        return u'%s %s %s %s %d %s' % (self.project_name, self.aliases_name, self.business_name, self.business_aliases_name, self.use_name, self.comment)

    class Meta:
        verbose_name = u"项目管理"
        verbose_name_plural = verbose_name
        app_label = 'assets'

SERVER_STATUS = (
    (0, "系统未安装"),
    (1, "已初始化"),
    (2, "正在运行"),
    (3, "下架")
)

BOOL_CHOICES = (
    (True, "使用中"),
    (False, "空闲")
)

SYSTEM_CHOICES = (
    (0, "CentOS"),
    (1, "Windows"),
    (2, "Ubuntu"),
)

class Host(models.Model):
    host_name = models.CharField(max_length=64, blank=True, null=True, verbose_name="主机名")
    idc = models.ForeignKey(IDC, blank=True, null=True, verbose_name="机房", on_delete=models.SET_NULL)
    eth1 = models.GenericIPAddressField(protocol="IPV4", null=True, verbose_name="IP地址", unique=True)
    eth2 = models.GenericIPAddressField(blank=True, null=True, verbose_name="IP地址2", default='null', unique=True)
    cpu = models.CharField(max_length=64, blank=True, null=True, verbose_name='CPU')
    memory = models.CharField(max_length=64, blank=True, null=True, verbose_name="内存")
    hard_disk = models.CharField(max_length=64, blank=True, null=True, verbose_name='硬盘')
    system = models.IntegerField(choices=SYSTEM_CHOICES, default=0, blank=True, null=True, verbose_name="系统类型")
    system_version = models.CharField(max_length=64, blank=True, null=True, verbose_name="版本号")
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    end_time = models.DateTimeField(blank=True, null=True, verbose_name="结束时间")
    business = models.ForeignKey(Project, blank=True, null=True, verbose_name="所属业务", on_delete=models.SET_NULL)
    status = models.IntegerField(verbose_name="机器状态", choices=SERVER_STATUS, default=0, blank=True)
    idle = models.BooleanField(verbose_name="状态", choices=BOOL_CHOICES, default=False)
    editor = models.TextField(blank=True, null=True, verbose_name="备注")
