import requests
from django.shortcuts import render
from django.http import HttpResponse
from future import config
import json

# Create your views here.

def index(request):

    return render(request, 'display/index.html')

def login(request):
    if request.method == 'GET':
        params = {'name': 'root', "password": 'Aa123456', }
        head = {"Content-type": "application/json"}
        r = requests.post("%s/user/login" % (config.API_ADDR), data=json.dumps(params), headers=head)
        print(request.session)
        request.session= r.json()
        print(request.session['name'])
        print(r, r.text, 'aa', r.status_code)
        return HttpResponse(r.text)
def chartdisplay(request):

    return render(request, 'display/index.html')