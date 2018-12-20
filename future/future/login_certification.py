#用户登录验证装饰器

from django.shortcuts import redirect


def auth(func):
    def inner(request, *args, **kwargs):
        status = request.session.get('is_login', None)
        if status == None:
            return redirect('/login/')
        else:
            return func(request, *args, **kwargs)
    return inner
