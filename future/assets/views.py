# -*- coding:utf-8 -*-
# author: "Xianglei Kong"
# 2019-01-11

from django.shortcuts import render, redirect, HttpResponse
from future.login_certification import auth
from . import models
from .form import IDC_form, Project_form, Host_from
from . import paging, paging1, page_change
from django.db import IntegrityError
import json

Host_per_page = 5       #定义host list显示的每页个数（全局变量）


def get_diff(obj1, obj2, username):
    text_list = []
    da1, da2 = obj1, obj2.dict()
    id = obj1['id']
    for k, v in da1.items():
        field = models.Host._meta.get_field(k).verbose_name ## 获取表单lable
        # print(field)
        if str(v) != da2.get(k):
            if k == "idc":
                old = models.IDC.objects.filter(id=v)
                new = models.IDC.objects.filter(id=da2.get(k))
                if old:
                    old_name = old[0].name
                else:
                    old_name = u'无'
                if new:
                    new_name = new[0].name
                else:
                    new_name = u'无'
                text = field + u'由' + old_name + u'更改为' + new_name
            elif k == "id":
                continue
            elif k == "business":
                old = models.Project.objects.filter(id=v)
                new = models.Project.objects.filter(id=da2.get(k))
                print(old)
                print(new)
                if old:
                    old_name = old[0].project_name
                else:
                    old_name = u'无'
                if new:
                    new_name = new[0].project_name
                else:
                    new_name = u'无'
                text = field + u'由' + old_name + u'更改为' + new_name
            elif k == "server_type":
                old_name = models.SERVER_TYPE[v][1]
                new_name = models.SERVER_TYPE[int(da2.get(k))][1]
                text = field + u'由' + old_name + u'更改为' + new_name
            elif k == "type":
                old_name = models.TYPE_CHOICES[v][1]
                new_name = models.TYPE_CHOICES[int(da2.get(k))][1]
                text = field + u'由' + old_name + u'更改为' + new_name
            elif k == "system":
                old_name = models.SYSTEM_CHOICES[v][1]
                new_name = models.SYSTEM_CHOICES[int(da2.get(k))][1]
                text = field + u'由' + old_name + u'更改为' + new_name
            elif k == "idle":
                if v == "True":
                    old_name = u"使用中"
                    new_name = u"空闲"
                else:
                    old_name = u"空闲"
                    new_name = u"使用中"
                text = field + u'由' + old_name + u'更改为' + new_name
            elif k == "status":
                old_name = models.SERVER_STATUS[v][1]
                new_name = models.SERVER_STATUS[int(da2.get(k))][1]
                text = field + u'由' + old_name + u'更改为' + new_name
            else:
                text = field + u'由' + str(v) + u'更改为' + str(da2.get(k))
            text_list.append(text)

    if len(text_list) != 0:
        models.Host_Record.objects.create(user=username, host_id=id, content=text_list)
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
            return render(request, 'assets/host_add.html', {'host_form': obj})
        else:
            obj.save()
            return redirect("/assets/host/add/")

@auth
def host_list(request):
    global Host_per_page
    if request.method == "GET":
        current_page = int(request.GET.get('p', 1))  # 获取当前页码
        num = models.Host.objects.all().count()  # 数据库数据个数
        url = "/assets/host/list/"
        per_page = Host_per_page  # 每页显示个数
        page_num = 7  # 页数标签个数
        page_obj = paging1.Page(current_page, num, per_page, page_num, url)
        host_info = models.Host.objects.filter()[page_obj.start():page_obj.end()]
        page_str = page_obj.page_str()
        idc_name = models.IDC.objects.values("id", "name").distinct()
        project_name = models.Project.objects.values("id", "project_name")
        host_num = models.Host.objects.filter().count()
        physic_num = models.Host.objects.filter(type=1).count()
        vm_num = models.Host.objects.filter(type=0).count()
        services = models.SERVER_TYPE
        server_status = models.SERVER_STATUS
        brands = models.SYSTEM_CHOICES
        host_type = models.TYPE_CHOICES
        return render(request, "assets/host_list.html", {
                                                         'host_info': host_info,
                                                         'page_str': page_str,
                                                         'host_num': host_num,
                                                         'physic_num': physic_num,
                                                         'vm_num': vm_num,
                                                         'idc_name': idc_name,
                                                         'project_name': project_name,
                                                         'services': services,
                                                         'server_status': server_status,
                                                         'brands': brands,
                                                         'host_type': host_type,
                                                         })

def host_del_batch(request):
    if request.method == "POST":
        data = request.POST.get('ids')
        print(data)
        del_id = data.split(',')
        for i in del_id:
            print(i)
        print(del_id)
        return HttpResponse('nice')
    if request.method == "GET":
        return HttpResponse('请求错误')

def host_search(request):
    global Host_per_page
    if request.method == "GET":
        data = request.GET
        change_idc = request.GET.get("change_idc")
        change_business = request.GET.get("change_business")
        change_service = request.GET.get("change_service")
        change_status = request.GET.get("change_status")
        change_brand = request.GET.get("change_brand")
        change_type = request.GET.get("change_type")
        status = request.GET.get("status", '')
        current_page = int(request.GET.get("p", 1))
        print("下面是P的值", current_page)
        page_str = 1
        host_dict = {"idc_id": change_idc, "business_id": change_business, "server_type": change_service, "status": change_status, "system": change_brand, "type": change_type}
        select = {}
        for key, value in host_dict.items():
            if value != "all":
                select[key] = value
        print(change_idc, change_business, change_service, change_status, change_brand, change_type)
        print(select)
        host_info = models.Host.objects.filter(**select)[(current_page-1)*Host_per_page:current_page*Host_per_page]
        if status:
            current_page = int(request.GET.get('p', 1))  # 获取当前页码
            num = models.Host.objects.filter(**select).count()  # 数据库数据个数
            url = "/assets/host/list/"
            per_page = Host_per_page  # 每页显示个数
            page_num = 7  # 页数标签个数
            page_obj = page_change.Page(current_page, num, per_page, page_num, url)
            page_str = page_obj.page_str()
            return render(request, "assets/host_page.html", locals())
        return render(request, "assets/host_info_ajax.html", locals())

@auth
def host_detail(request):
    if request.method == ('GET'):
        uuid = int(request.GET.get('uuid', 1))
        host = models.Host.objects.filter(id=uuid).first()
        host_record = models.Host_Record.objects.filter(host_id=uuid).order_by('-time')
        return render(request, "assets/host_detail.html", {'host': host, "host_record": host_record})

def host_bak(request):
    return render(request, "assets/host_detail_bak.html")

def host_edit(request):
    if request.method == "GET":
        uuid = request.GET.get('uuid')
        if uuid == 0:
            return HttpResponse('错误输入')
        host = models.Host.objects.get(id=uuid)
        host_form = Host_from(instance=host)
        return render(request, "assets/host_edit.html", {"host_form": host_form})
    if request.method == "POST":
        data = {'status': False, 'message': ''}
        uuid = request.GET.get('uuid')
        host = models.Host.objects.get(id=uuid)
        form = Host_from(instance=host, data=request.POST)
        try:
            form.save()
            if form.is_valid():
                # print(form.__dict__.get("initial"))
                # print(request.POST.dict())
                username = request.session['username']
                get_diff(form.__dict__.get('initial'), request.POST, username)
                data['status'] = True
                return HttpResponse(json.dumps(data))
            else:
                return HttpResponse(json.dumps(data))
        except Exception as e:
            data['message'] = str(e)
            return HttpResponse(json.dumps(data))

def host_del(request):
    if request.method == ('POST'):
        id = int(request.POST.get('id'))
        print(id)
        return HttpResponse('nice')