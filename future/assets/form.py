from django import forms
from .models import idc_operator, idc_type

class IDC_form(forms.Form):
    idc_name = forms.CharField(label='机房名称', max_length=64,  widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '机房名称'}))
    idc_area = forms.CharField(label='机房地址', max_length=128,  widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '机房地址'}))
    idc_operator = forms.ChoiceField(label="运营商", choices=idc_operator, widget=forms.Select(attrs={'class': 'form-control select2 select2-hidden-accessible', 'style': 'width: 100%;', 'tabindex': '-1', 'ria-hidden': 'true'}))
    idc_type = forms.ChoiceField(label="机房类型", choices=idc_type,  widget=forms.Select(attrs={'class': 'form-control select2 select2-hidden-accessible', 'style': 'width: 100%;', 'tabindex': '-1', 'ria-hidden': 'true'}))
    idc_comment = forms.CharField(label="备注", required=False, widget=forms.Textarea(attrs={'class': 'textarea form-control', 'style': 'width: 100%;'}))

