from django.shortcuts import render,HttpResponse
import json


# Create your views here.

def login(request):
    if request.method == 'GET':
        return render(request, 'login/login.html')
    if request.method == "POST":
        # print(request.method.data)
        data = {'status': False, 'message': 'nice to meet you'}
        return HttpResponse(json.dumps(data))

