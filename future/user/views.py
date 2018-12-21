from django.shortcuts import render,HttpResponse

# Create your views here.

def add(request):
    return render(request, 'user/user_add.html')

def change(request):
    return HttpResponse('change')
