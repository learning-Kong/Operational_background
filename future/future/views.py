from django.shortcuts import HttpResponseRedirect

def log_302(request):
    return HttpResponseRedirect('/login/')

