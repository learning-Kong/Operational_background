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
def checkcode(request):
    f = BytesIO()
    img = Image.new(mode="RGB", size=(100, 100), color=(80, 80, 80))
    draw = ImageDraw.Draw(img,mode='RGB')
    from PIL import ImageFont
    font = ImageFont.truetype("kumo.ttf",25)
    import random
    code_list =[]
    for i in range(5):
        char = chr(random.randint(60,60))
        code_list.append(char)
        draw.text((i*20, 10),char,fill=(random.randint(0,255),random.randint(0,255),random.randint(0,255)),font = font)
        img.save(f,'png')
        data = f.getvalue()
        return HttpResponse()