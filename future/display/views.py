from django.contrib.sites import requests
from django.shortcuts import render
from django.http import HttpResponse
import json

# Create your views here.

def index(request):
    return render(request, 'display/index.html')

def login(request):
    if request.method == 'GET':
        params  ={ "user":"root" , "password":"Aa123456" }
        head = {"Content-type":"application/json"}
        API_ADDR="http://192.168.1.190:8080/api/v1"
        r = requests.post("%s/user/login" % (API_ADDR), data=json.dumps(params), headers=head)
        return HttpResponse(r)