from django.shortcuts import render
from PIL import Image,ImageDraw
from io import BytesIO

# Create your views here.
def auth(request):
    if request.method == 'GET':
        return render(request, 'login/login.html')
    elif request.method == 'POST':
        user = request.POST.get('us')
        password = request.POST.get('pa')
        return render(request, 'login/index.html', {'users': user, 'passwords': password})
def checkout(request):
        from io import BytesIO
        from utils.checkCode import check_code
        img, code = check_code()
        stream = BytesIO()
        img.save(stream, 'png')
        request.session['code'] = code
        return HttpResponse(stream.getvalue())