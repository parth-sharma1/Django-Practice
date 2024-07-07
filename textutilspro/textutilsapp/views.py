from django.shortcuts import render, HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("Hello this is an index page")


def removepunc(request):
    return HttpResponse("Hello this is removepunc page")


def capitalizefirst(request):
    return HttpResponse("Hello this is an capitalize page")


def newlineremove(request):
    return HttpResponse("Hello this is newlineremove page")


def spaceremove(request):
    return HttpResponse("Hello this is spaceremove page")


def charcount(request):
    return HttpResponse("Hello this is an charactercount page")


