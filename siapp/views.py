from django.shortcuts import render
def index(request):
    return render(request,"siapp/index.html")
def sicode(request):
    p = request.GET["txtp"]
    r = request.GET["txtr"]
    t = request.GET["txtt"]
    si = (float(p)*float(r)*float(t))/100
    return render(request,"siapp/index.html",{"res":si}) 

def additionload(request):
    return render(request,"siapp/additionload.html")       

def additionlogic(request):
    a = request.GET["txtnum1"]
    b = request.GET["txtnum2"]
    c = int(a) + int(b)
    return render(request,"siapp/additionload.html",{"res":c})