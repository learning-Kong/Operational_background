from django.shortcuts import render, HttpResponse
from future.login_certification import auth
import json
import re
from login import models
from . import paging

# Create your views here.

@auth
def add(request):
    if request.method == "GET":
        Groupinfo = models.UserGroup.objects.filter()
        return render(request, 'user/user_add.html', {'Groupinfo': Groupinfo})
    if request.method == "POST":
        pwd_null = '01b1f2dd8ba23c813b13a2e2e55f8af457b0f9daa925ec67bf16d7348c11a25c'
        data = {'status': False, 'message': 'nice to meet you'}
        User_name = request.POST.get('username')
        User_tel = request.POST.get('tel')
        User_email = request.POST.get('email')
        User_password = request.POST.get('pwd')
        User_re_password = request.POST.get('re_pwd')
        Gid = request.POST.get('value')
        pwd_db = models.User.objects.filter(name=User_name).first()
        if not pwd_db:
            if User_name != '':
                if re.fullmatch(r"1\d{10}", User_tel):
                    if re.match(r'^[0-9a-zA-Z_]{0,19}@[0-9a-zA-Z]{1,13}\.[com,cn,net]{1,3}$', User_email):
                        if User_password == User_re_password:
                            if User_password != pwd_null:
                                models.User.objects.create(name=User_name, password=User_password, email=User_email, tel=User_tel, G_id = Gid)
                                data['status'] = True
                            else:
                                data['message'] = '密码不能为空'
                        else:
                            data['message'] = '两次输入的密码不一样'
                    else:
                        data['message'] = '输入的Emil格式不正确'
                else:
                    data['message'] = '输入的电话号码不正确'
            else:
                data['message'] = '用户名不能为空'
        else:
            data['message'] = '用户名已存在'
        return HttpResponse(json.dumps(data))

@auth
def change(request):
    if request.method == "GET":
        current_page = int(request.GET.get('p', 1)) #获取当前页码
        num = models.User.objects.all().count() #数据库数据个数
        per_page = 10    #每页显示个数
        page_num = 7    #页数标签个数
        page_obj = paging.Page(current_page, num, per_page, page_num)

        pwd_db = models.User.objects.all()[page_obj.start():page_obj.end()]
        page_str = page_obj.page_str()
        print(page_str)
        return render(request, 'user/user_change.html', {'pwd_db': pwd_db, 'page_str': page_str})
