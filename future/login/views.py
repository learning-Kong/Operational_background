from django.shortcuts import render
from django.http import HttpResponse

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
        from .models.authimages import check_code
        img, code = check_code()
        stream = BytesIO()
        img.save(stream, 'png')
        request.session['code'] = code
        return HttpResponse(stream.getvalue())