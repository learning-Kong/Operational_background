from django.shortcuts import render,HttpResponse,HttpResponseRedirect

# Create your views here.

def login(request):
    return render(request, 'login/login.html')

# def log_302(request):
#     return HttpResponseRedirect('/login/')
