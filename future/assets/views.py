from django.shortcuts import render, redirect
from future.login_certification import auth
from . import models
from .form import IDC_form

# Create your views here.
@auth
def list(request):
    if request.method == "POST":
        obj = IDC_form(request.POST)
        if obj.is_valid():
            idc_name = request.POST.get('idc_name')
            idc_area = request.POST.get('idc_area')
            idc_operator = request.POST.get('idc_operator')
            idc_type = request.POST.get('idc_type')
            idc_comment = request.POST.get('idc_comment')
            print(idc_name, idc_area, idc_operator, idc_type, idc_comment)
            models.IDC.objects.create(name=idc_name, address=idc_area, operator=idc_operator, type=idc_type, comment=idc_comment)
            return redirect('/assets/idc_list/')
    else:
        idc_form = IDC_form()
        return render(request, 'assets/idc_add.html', {'idc_form': idc_form})
