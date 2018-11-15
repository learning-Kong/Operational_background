from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def auth(request):
    if request.method == 'GET':
        return render(request, 'login/login.html')
    elif request.method == 'POST':
        user = request.POST.get('user')
        password = request.POST.get('password')
        (pubkey, privkey) = rsa.newkeys(1024)
        return render(request, 'login/index.html', {'users': user, 'passwords': password, 'session':request.session.get('code'), 'rsapub': pubkey.save_pkcs1(), 'rsaprivate': privkey.save_pkcs1()})
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

