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