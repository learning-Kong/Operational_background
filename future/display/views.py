import requests
from django.shortcuts import render
from django.http import HttpResponse
from future import config
import pandas as pd
import numpy as np
from numpy import nan as NaN
import time
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
    t = int(time.time())
    params= {"step": 60,"start_time": 1547461220,"hostnames": ["test"],"end_time": 1547461320,"counters": ["cpu.idle"],"consol_fun": "AVERAGE"}
    head = {'Apitoken':json.dumps({"name":"root","sig":"e55a622decc811e8aef5000c2913d5c4"}),'X-Forwarded-For':'192.168.1.190',"Content-Type": "application/json"}
    print('\n','aaaaaaaaaaaa')
    r = requests.post("%s/graph/history" % (config.API_ADDR), data=json.dumps(params), headers=head)
    a=r.json()
    print(a[0]['Values'])
    tlist=[]
    vlist=[]
    b=a[0]['Values']
    test= pd.DataFrame(b)
    print(test,type(test))
    # for x in test:
    #     tlist.append(x['timestamp'])
    #
    #     vlist.append( x['value'])
    #     print(x['timestamp'])
    #     print(x['value'])
    #print(r.text,'\n',a[0]['Values'])
    #print(tlist,vlist)
    print(int(t))
    #return HttpResponse(r.text)
    #return render(request, 'display/chart.html',{'tlist': tlist,'vlist':vlist})
    return render(request, 'display/chart.html',{'tlist': test.timestamp,'vlist':test.value})
def chartss(request):
    return render(request, 'display/chart test.html')