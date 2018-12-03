from django.shortcuts import render
from django.http import HttpResponse
from . import models
from .tsetsmodels.authmodels import auths

# Create your views here.
def test(request):
    if request.method == 'GET':
        return render(request, 'tests/test.html')
    elif request.method == 'POST':
        user=request.POST.get('user')
        password=request.POST.get('password')
        #dbpassword = models.User.objects.get(password=password)
        try:
            dbuser = models.User.objects.get(username=user, password=password)
            request.session=dbuser.all()
            print(request.session)
            return render(request, 'tests/indexs.html', {'user': dbuser.username, 'password': dbuser.password})
        except:
            return HttpResponse('test')

@auths(pages1='test01' ,user1='test')
def aa(request):
    return HttpResponse('test')