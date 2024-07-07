from django.shortcuts import render, HttpResponse, redirect

# Create your views here.

def index(request):
    context = {'name':"parth", "place":"moradabad"}
    return  render(request, "index.html", context)


def analyze(request):
    # get the text
    text = (request.GET.get("textarea"))
    removepunc = (request.GET.get("removepunc", "off"))
    print(removepunc)
    print(text)

    if removepunc == "on":
    
        punctuations = '''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''
        analyzed = ""
        for char in text:
            if char not in punctuations:
                analyzed = analyzed+char


        params = {'purpose':'removed punctuations', "analysed_text":analyzed}

        # analyze the text
        return render(request, "analyze.html", params)
    else:
        return HttpResponse("Error")


# def capitalizefirst(request):
#     return HttpResponse("Hello this is an capitalize page")


# def newlineremove(request):
#     return HttpResponse("Hello this is newlineremove page")


# def spaceremove(request):
#     return HttpResponse("Hello this is spaceremove page")


# def charcount(request):
#     return HttpResponse("Hello this is an charactercount page")


