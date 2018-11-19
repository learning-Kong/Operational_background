from django.shortcuts import render
from django.http import HttpResponse
from future import config

# Create your views here.
def auth(request):
    if request.method == 'GET':
        return render(request, 'login/login.html')
    elif request.method == 'POST':
        user = request.POST.get('user')
        password = request.POST.get('password')
        return render(request, 'login/index.html', {'users': user, 'passwords': password, 'session':request.session.get('code')})
def checkout(request):
    from io import BytesIO
    from .viewmodels.authimages import check_code
    img, code = check_code()
    stream = BytesIO()
    img.save(stream, 'png')
    request.session['code'] = code
    return HttpResponse(stream.getvalue())
def index(request):
    return render(request, 'login/indexs.html')
def logins(request):
    if request.method == 'GET':
        return render(request, 'login/login.html')
    elif request.method == 'POST':
        user = request.POST.get('user')
        password = request.POST.get('password')
        params = { 'name': user, "password": password, }
        r = request.post("%s/user/login" %config.API_ADDR,data = params)
        if r.status_code != 200:
            raise Exception("%s : %s" % (r.status_code, r.text))
        j = r.json()
        return j
