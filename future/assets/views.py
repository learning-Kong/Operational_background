from django.shortcuts import render, redirect, HttpResponse
from future.login_certification import auth
from . import models
from .form import IDC_form
from . import paging

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
        idc_status = models.IDC.objects.filter(id=idc_id).first()
        if not idc_status:
            return HttpResponse('需要修改的主机不存在')
        else:
            idc_form = IDC_form(initial={'idc_id': idc_status.id, 'idc_name': idc_status.name, 'idc_area': idc_status.address, 'idc_comment': idc_status.comment, 'idc_operator': idc_status.operator, 'idc_type': idc_status.type})
            return render(request, "assets/idc_change.html", {"idc_form": idc_form})

@auth
def idc_del(request):
    if request.method == "GET":
        print(1)
        idc_id = int(request.GET.get('idc_id', 0))
        if idc_id == 0:
            return HttpResponse('需要修改的主机不存在')
        else:
            models.IDC.objects.filter(id=idc_id).delete()
            return redirect('/assets/idc_list/')
