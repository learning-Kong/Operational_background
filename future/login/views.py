from django.shortcuts import render,HttpResponse,HttpResponseRedirect

# Create your views here.

def login(request):
    return HttpResponse('Hello word! nice')

def log_302(request):
    return HttpResponseRedirect('/login/')
