from django.shortcuts import render,HttpResponse

# Create your views here.

def add(request):
    return HttpResponse('ok')

def change(request):
    return HttpResponse('change')
