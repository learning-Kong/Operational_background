from django.shortcuts import render
from django.http import HttpResponse
from . import models
from .models import User

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
            return render(request, 'tests/indexs.html', {'user': dbuser.username, 'password': dbuser.password})
        except:
            return HttpResponse('test')