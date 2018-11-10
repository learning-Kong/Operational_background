from django.shortcuts import render


# Create your views here.
def auth(request):
    if request.method == 'GET':
        return render(request, 'login/login.html')
    elif request.method == 'POST':
        user = request.POST.get('us')
        password = request.POST.get('pa')
        return render(request, 'login/index.html', {'users': user, 'passwords': password})
