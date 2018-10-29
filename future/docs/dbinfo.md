# 用户表
## user表结构设计
```
+-------------------+--------------+------+-----+---------+-------+
| Field             | Type         | Null | Key | Default | Extra |
+-------------------+--------------+------+-----+---------+-------+
| userid            | char(32)     | NO   | PRI | NULL    |       |      #用户id
| username          | varchar(50)  | NO   |     | NULL    |       |      #用户名
| userpassword      | char(16)     | YES  |     | NULL    |       |      #密码
| phonenumber       | char(13)     | YES  |     | NULL    |       |      #电话号码
| email             | varchar(30)  | YES  |     | NULL    |       |      #邮件
+-------------------+--------------+------+-----+---------+-------+
```

