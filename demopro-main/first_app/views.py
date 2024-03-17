from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import Contact
from first_app.models import Contact2
from first_app.models import Res

# Create your views here.
def fun(request):
    return HttpResponse("Hello from first django project")
def launch(request):
    # set variable jo template m bhejte hai
    context={
        'variable':"this is sent"
    }
    return render(request,"home.html",context)
def about(request):
    return render(request,"about.html")
    #return HttpResponse("About us")
def services(request):
    return render(request,"services.html")
    #return HttpResponse("services")
def contact(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        contact=Contact(name=name, email=email, phone=phone)
        contact.save()
    return render(request,"contact.html")
    #return HttpResponse("contacts")
def success(request):
    name=request.GET['user']
    return HttpResponse("LOGIN SUCCESSFUL...!!WELCOME {}".format(name))
def web2(request):
    if request.method=="POST":
        name2=request.POST.get('name2')
        email2=request.POST.get('email2')
        phone2=request.POST.get('phone2')
        web2=Contact2(name2=name2, email2=email2, phone2=phone2)
        web2.save()
    return render(request,"web2.html")
def zomato(request):
     if request.method=="POST":
            Restaurant=request.POST.get('Restaurant')
            zomato=Res( Restaurant= Restaurant)
            zomato.save()
     return render(request,"zomato.html")

