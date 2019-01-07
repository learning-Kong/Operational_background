from django.db import models

# Create your models here.

class UserGroup(models.Model):
    department = models.CharField(max_length=256, verbose_name='部门')
    position = models.CharField(max_length=256, verbose_name='职位')
    permission = models.IntegerField(default=2, verbose_name='权限')

    def __str__(self):
        return u'%s %s %d' % (self.department, self.position, self.permission)

    class Meta:  # 定义表名
        verbose_name = '人员管理'
        verbose_name_plural = '人员管理'

class User(models.Model):
    gender = (('male', '男'), ('female', '女'))
    name = models.CharField(max_length=123, unique=True)
    password = models.CharField(max_length=256)
    email = models.EmailField()
    tel = models.CharField(max_length=11, default=None)
    sex = models.CharField(max_length=32, choices=gender, default='男')
    create_time = models.DateTimeField(auto_now_add=True)
    G = models.ForeignKey(to_field='id', to="UserGroup", on_delete=models.CASCADE, default=1)
