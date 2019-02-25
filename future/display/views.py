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
    params= {"step": 60,"start_time": 1548112805,"hostnames": ["localhost.localdomain"],"end_time": 1549894805,"counters": ["cpu.idle"],"consol_fun": "AVERAGE"}
    head = {'Apitoken':json.dumps({"name":"root","sig":"13953a520ff211e9917686bf05b23eb4"}),'X-Forwarded-For':'192.168.15.156',"Content-Type": "application/json"}
    print('\n','aaaaaaaaaaaa')
    r = requests.post("%s/graph/history" % (config.API_ADDR), data=json.dumps(params), headers=head)
    a=r.json()
    print(a)
    print(a[0]['Values'])
    # tlist=[]
    # vlist=[]
    b=a[0]['Values']
    #
    test= pd.DataFrame(b)
    # print(test.where(test.notnull(),NaN))
    test=test.where(test.notnull(),NaN)
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
    #return render(request, 'display/chart.html',{'tlist': test.timestamp.tolist(),'vlist':test.value.tolist()})
    return HttpResponse(json.dumps(a))
def chartss(request):
    return render(request, 'display/chart test.html')

def ajaxchart(request):
    return render(request, 'display/ajax.html')