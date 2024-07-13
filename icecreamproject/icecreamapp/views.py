from django.shortcuts import render, HttpResponse, redirect
from icecreamapp.models import Contact
from django.contrib import messages
from datetime import datetime


# Create your views here.
def index(request):
    context = {      
        "variable1": "this is variable1",
        "variable2": "this is variable2"
    }

    return render(request, 'index.html', context)
    # return HttpResponse("this is home page")

def about(request):
    #return HttpResponse("this is about page")
    return render(request, 'about.html')

def services(request):
    #return HttpResponse("this is services page")
    return render(request, 'services.html')


def contact(request):
    #return HttpResponse("this is contact page")

    if request.method=="POST":
        firstname = request.POST.get("firstname")
        lastname = request.POST.get("lastname")
        email = request.POST.get("email")
        address = request.POST.get("address")
        phone = request.POST.get("phone")
        desc = request.POST.get("desc")
        city = request.POST.get("city")
        state = request.POST.get("state")
        pincode = request.POST.get("pincode")

        contact = Contact(firstname = firstname, lastname =lastname, email=email, address = address, phone=phone, desc = desc, city=city, state=state, pincode=pincode, date= datetime.today())
        contact.save()
        messages.success(request, "Your message has been sent!")

    return render(request, 'contact.html')
