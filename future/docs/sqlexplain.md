### 1、table user

|字段|对应意义|
|-----|---------|
|userid|用户id（唯一标识）|
|username|用户名|
|password|密码|
|email|邮箱|

### 2、table group

|字段|对应意义|
|-----|---------|
|groupid|组id（唯一标识）|
|userid|用户id|
|department|部门|

### 3、table authorityinfo

|字段|对应意义|
|-----|---------|
|authorityid|权限模块id|
|authorityname|权限模块名称|

### 4、table authority

|字段|对应意义|
|-----|---------|
|userid|用户id|
|groupid|组id|
|authorityid|权限模块id|