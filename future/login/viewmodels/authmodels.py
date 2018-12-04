from .. import models
from django.shortcuts import render

def auths(pages1):
    def authtest(func):
        def authpages(request):
            try:
                print('pages1:s%',pages1)
                print('request:s%',request.session['username'])
                models.Memberships.objects.get(user__username=request.session['username'], authorityinfo__authorityname=pages1)
                return  func(request)
            except:
                return render(request,'tests/indexs.html',{'user':request.session['username'],'password':pages1})
        return authpages
    return authtest