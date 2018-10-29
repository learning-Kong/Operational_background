# 资产管理
## user表结构设计
```
+-------------------+--------------+------+-----+---------+-------+
| Field             | Type         | Null | Key | Default | Extra |
+-------------------+--------------+------+-----+---------+-------+
| userid            | char(32)     | NO   | PRI | NULL    |       |      #用户id
| username          | varchar(100) | NO   |     | NULL    |       |      #用户名
| userpassword      | char(15)     | YES  |     | NULL    |       |      #密码
| phonenumber       | char(15)     | YES  |     | NULL    |       |      #电话号码
| email             | varchar(20)  | YES  |     | NULL    |       |      #邮件
+-------------------+--------------+------+-----+---------+-------+
```

