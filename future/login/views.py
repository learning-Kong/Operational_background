from django.shortcuts import render
from django.http import HttpResponse
from .viewmodels.privatersakey import prvidekey

from crypto.library.cryptor import Cryptor

# Create your views here.
def auth(request):
    if request.method == 'GET':
        return render(request, 'login/login.html')
    elif request.method == 'POST':
        user = request.POST.get('user')
        password = request.POST.get('password')
        rsapub,rsaprivte= prvidekey()
        return render(request, 'login/index.html', {'users': user, 'passwords': password, 'session':request.session.get('code'),'pubp':rsapub,'pubpr':rsaprivte})
def checkout(request):
        from io import BytesIO
        from .viewmodels.authimages import check_code
        img, code = check_code()
        stream = BytesIO()
        img.save(stream, 'png')
        request.session['code'] = code
        return HttpResponse(stream.getvalue())