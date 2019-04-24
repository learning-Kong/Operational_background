# -*- coding:utf-8 -*-
# author: "Xianglei Kong"

from django import forms
from .models import idc_operator, idc_type, use_type
from . import models

class IDC_form(forms.Form):
    idc_id = forms.IntegerField(initial=0, widget=forms.TextInput(attrs={'class': 'hide'}))
    idc_name = forms.CharField(label='机房名称', max_length=64,  widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '机房名称'}))
    idc_area = forms.CharField(label='机房地址', max_length=128,  widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '机房地址'}))
    idc_operator = forms.ChoiceField(label="运营商", choices=idc_operator, widget=forms.Select(attrs={'class': 'form-control select2 select2-hidden-accessible', 'style': 'width: 100%;', 'tabindex': '-1', 'ria-hidden': 'true'}))
    idc_type = forms.ChoiceField(label="机房类型", choices=idc_type,  widget=forms.Select(attrs={'class': 'form-control select2 select2-hidden-accessible', 'style': 'width: 100%;', 'tabindex': '-1', 'ria-hidden': 'true'}))
    idc_comment = forms.CharField(label="备注", required=False, widget=forms.Textarea(attrs={'class': 'textarea form-control', 'style': 'width: 100%;'}))

class Project_form(forms.Form):
    project_name = forms.CharField(label='项目名称', max_length=64, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '项目名称'}))
    aliases_name = forms.CharField(label='项目简称', max_length=64, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '项目简称'}))
    business_name = forms.CharField(label='业务名称', max_length=64, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '业务名称'}))
    business_aliases_name = forms.CharField(label='业务名简称', max_length=64, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '业务简称'}))
    use_name = forms.ChoiceField(label="业务用途", choices=use_type, widget=forms.Select(attrs={'class': 'form-control select2 select2-hidden-accessible', 'style': 'width: 100%;', 'tabindex': '-1', 'ria-hidden': 'true'}))
    comment = forms.CharField(label="备注", required=False, widget=forms.Textarea(attrs={'class': 'textarea form-control', 'style': 'width: 100%;'}))

class Host_from(forms.ModelForm):
    class Meta:
        model = models.Host
        # fields = '__all__'
        exclude = ["eth2", "create_time", "end_time"]

        widgets = {
            "host_name": forms.TextInput(attrs={'class': 'form-control'}),
            "type": forms.Select(attrs={'class': 'form-control'}),
            "idc": forms.Select(attrs={'class': 'form-control'}),
            "eth1": forms.TextInput(attrs={'class': 'form-control '}),
            "internal_ip": forms.TextInput(attrs={'class': 'form-control '}),
            "cpu": forms.TextInput(attrs={'class': 'form-control'}),
            "memory": forms.TextInput(attrs={'class': 'form-control'}),
            "hard_disk": forms.TextInput(attrs={'class': 'form-control'}),
            "system": forms.Select(attrs={'class': 'form-control'}),
            "system_version": forms.TextInput(attrs={'class': 'form-control'}),
            "business": forms.Select(attrs={'class': 'form-control'}),
            "server_type": forms.Select(attrs={'class': 'form-control'}),
            "status": forms.Select(attrs={'class': 'form-control'}),
            "idle": forms.Select(attrs={'class': 'form-control'}),
            "editor": forms.Textarea(attrs={'class': 'textarea form-control'}),
        }

        error_messages = {
            'eth1': [{"code": "required", "message": "请输入一个有效的 IPV4 地址"}],
            'internal_ip': [{"code": "required", "message": "请输入一个有效的 内网 地址"}]
        }

