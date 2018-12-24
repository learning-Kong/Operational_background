from django.shortcuts import render,HttpResponse
from future.login_certification import auth
# Create your views here.

@auth
def add(request):
    if request.method == "GET":
        return render(request, 'user/user_add.html')
    if request.method == "POST":
        print('OK')

def change(request):
    return HttpResponse('change')
