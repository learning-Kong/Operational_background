# -*- coding:utf-8 -*-
# author: "Xianglei Kong"
# 2019-01-11

from django.shortcuts import render, redirect, HttpResponse
from future.login_certification import auth
from . import models
from .form import IDC_form, Project_form, Host_from
from . import paging, paging1
from django.db import IntegrityError

# Create your views here.
@auth
def idc_add(request):
    if request.method == "POST":
        obj = IDC_form(request.POST)
        if obj.is_valid():
            idc_name = request.POST.get('idc_name')
            idc_area = request.POST.get('idc_area')
            idc_operator = request.POST.get('idc_operator')
            idc_type = request.POST.get('idc_type')
            idc_comment = request.POST.get('idc_comment')
            idc_id = request.POST.get('idc_id')
            print(idc_name, idc_area, idc_operator, idc_type, idc_comment, idc_id)
            if int(idc_id) == 0:
                models.IDC.objects.create(name=idc_name, address=idc_area, operator=idc_operator, type=idc_type, comment=idc_comment)
                # models.IDC.objects.create(**obj.cleaned_data)
            else:
                models.IDC.objects.filter(id=idc_id).update(name=idc_name, address=idc_area, operator=idc_operator, type=idc_type, comment=idc_comment)
            return redirect('/assets/idc_list/')
        return HttpResponse('请求错误')
    else:
        idc_form = IDC_form()
        return render(request, 'assets/idc_add.html', {'idc_form': idc_form})

@auth
def idc_list(request):
    if request.method == "GET":
        current_page = int(request.GET.get('p', 1))  # 获取当前页码
        num = models.IDC.objects.all().count()  # 数据库数据个数
        per_page = 10  # 每页显示个数
        page_num = 7  # 页数标签个数
        page_obj = paging.Page(current_page, num, per_page, page_num)
        idc_info = models.IDC.objects.filter()[page_obj.start():page_obj.end()]
        page_str = page_obj.page_str()
        # idc_info = models.IDC.objects.filter()
        return render(request, 'assets/idc_list.html', {'idc_info': idc_info, 'page_str': page_str})

@auth
def idc_change(request):
    if request.method == "GET":
        idc_id = int(request.GET.get('idc_id', 0)) #获取需要修改页面的值，默认为0
        status = int(request.GET.get('status'))
        print(status)
        idc_status = models.IDC.objects.filter(id=idc_id).first()
        if not idc_status or status != 1:
            return HttpResponse('需要修改的主机不存在')
        else:
            idc_form = IDC_form(initial={'idc_id': idc_status.id, 'idc_name': idc_status.name, 'idc_area': idc_status.address, 'idc_comment': idc_status.comment, 'idc_operator': idc_status.operator, 'idc_type': idc_status.type})
            return render(request, "assets/idc_change.html", {"idc_form": idc_form})

@auth
def idc_del(request):
    if request.method == "GET":
        idc_id = int(request.GET.get('idc_id', 0))
        idc_status = int(request.GET.get('status'))
        if idc_id == 0 or idc_status != 1:
            return HttpResponse('需要修改的IDC信息不存在')
        else:
            print('准备删除IDC机房')
            models.IDC.objects.filter(id=idc_id).delete()
            return redirect('/assets/idc_list/')

@auth
def project_add(request):
    if request.method == "GET":
        project_form = Project_form()
        return render(request, 'assets/project_add.html', {'project_form': project_form})
    else:
        obj = Project_form(request.POST)
        aliases_name = request.POST.get('aliases_name')
        project_id = request.POST.get('project_id')
        print(project_id)
        if obj.is_valid():  #检测form表单返回值是否正确
            try:
                if project_id:
                    project_dict = obj.cleaned_data
                    del project_dict['aliases_name']
                    print(project_dict)
                    models.Project.objects.filter(id=int(project_id)).update(**project_dict)
                else:
                    models.Project.objects.create(**obj.cleaned_data)
            except IntegrityError as e:#检测数据库主键冲突异常处理
                print(e)
                error_str = '项目简称   %s    已存在请重新处理' % aliases_name
                return HttpResponse(error_str)
            return redirect("/assets/project/list/")
        else:
            return HttpResponse('filed')

@auth
def project_edit(request):
    if request.method == "GET":
        project_id = int(request.GET.get('project_id', 0))
        status = int(request.GET.get('status'))
        if project_id == 0 or status != 2:
            return HttpResponse('需要修改的项目信息不存在')
        else:
            project_info = models.Project.objects.filter(id=project_id).first()
            project_form = Project_form(initial={'project_name': project_info.project_name, 'aliases_name': project_info.aliases_name, 'business_name': project_info.business_name, 'business_aliases_name': project_info.business_aliases_name, 'use_name': project_info.use_name, 'comment': project_info.comment})
            return render(request, 'assets/project_edit.html', {'project_form': project_form, 'project_id': project_id})

@auth
def project_list(request):
    if request.method == "GET":
        current_page = int(request.GET.get('p', 1))  # 获取当前页码
        num = models.Project.objects.all().count()  # 数据库数据个数
        url = "/assets/project/list/"
        per_page = 3  # 每页显示个数
        page_num = 7  # 页数标签个数
        page_obj = paging1.Page(current_page, num, per_page, page_num, url)
        project_info = models.Project.objects.filter()[page_obj.start():page_obj.end()]
        page_str = page_obj.page_str()

        return render(request, 'assets/project_list.html', {'project_info': project_info, 'page_str': page_str})

@auth
def project_del(request):
    if request.method == "GET":
        project_id = int(request.GET.get('project_id', 0))
        project_status = int(request.GET.get('status'))
        if project_id == 0 or project_status != 2:
            return HttpResponse('需要修改的IDC信息不存在')
        else:
            print('准备删除主机')
            models.Project.objects.filter(id=project_id).delete()
            return redirect('/assets/project/list/')

@auth
def host_add(request):
    if request.method == "GET":
        host_form = Host_from()
        return render(request, "assets/host_add.html", {"host_form": host_form})
    if request.method == "POST":
        obj = Host_from(request.POST)
        if not obj.is_valid():
            print(obj.is_valid())
            print(obj.errors)
            return render(request, 'assets/host_add.html', {'host_form': obj})
        else:
            obj.save()
            return HttpResponse(123)

@auth
def host_list(request):
    if request.method == "GET":
        current_page = int(request.GET.get('p', 1))  # 获取当前页码
        num = models.Host.objects.all().count()  # 数据库数据个数
        url = "/assets/host/list/"
        per_page = 3  # 每页显示个数
        page_num = 7  # 页数标签个数
        page_obj = paging1.Page(current_page, num, per_page, page_num, url)
        host_info = models.Host.objects.filter()[page_obj.start():page_obj.end()]
        print(host_info)
        for i in host_info:
            print(i.host_name)
        page_str = page_obj.page_str()
        return render(request, "assets/host_list.html", {'host_info': host_info, 'page_str': page_str})
