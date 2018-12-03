from .. import models
from django.shortcuts import render

def auths(pages1,user1):
    def authtest(func):
        def authpages(request):
            #try:
            print(pages1,user1)
            print(request)
            res = models.User.objects.get(username=user1)
            print(res.username)
            aut = models.Authorityinfo.objects.get(authorityname=pages1)
            rr = models.Memberships.objects.get(user_id=res, authorityinfo_id=aut.authorityid)
            #except:
                #return render(request,'tests/indexs.html',{'user':user1,'password':pages1})

        return authpages
    return authtest