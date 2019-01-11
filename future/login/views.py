# -*- coding:utf-8 -*-
# author: "Xianglei Kong"

from django.shortcuts import render,HttpResponse, redirect
import json
from . import models
from django.views.decorators.csrf import ensure_csrf_cookie
from future.login_certification import auth

# Create your views here.

@ensure_csrf_cookie
def login(request):
    if not request.session.get('is_login', None):
        if request.method == 'GET':
            return render(request, 'login/login.html')
        if request.method == "POST":
            pwd_null = '01b1f2dd8ba23c813b13a2e2e55f8af457b0f9daa925ec67bf16d7348c11a25c'
            data = {'status': False, 'message': 'nice to meet you'}
            User_name = request.POST.get('account_code')
            User_password = request.POST.get('pwd')
            if not User_name or User_password == pwd_null:
                data['message'] = "用户名或密码不能为空"
            else:
                pwd_db = models.User.objects.filter(name=User_name).first()
                if pwd_db:
                    if User_password == pwd_db.password:
                        data['status'] = True
                        request.session['username'] = User_name
                        request.session['is_login'] = True
                        request.session['department'] = pwd_db.G.department
                        request.session['position'] = pwd_db.G.position
                    else:
                        data['message'] = "密码错误"
                else:
                    data['message'] = "用户名不存在"
            return HttpResponse(json.dumps(data))
    return redirect('/login/home/')

@auth
def home(request):
        if request.method == "GET":
            return render(request, 'login/home.html')

@auth
def logout(request):
    request.session.flush()
    return redirect('/login/')
