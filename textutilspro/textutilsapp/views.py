from django.shortcuts import render, HttpResponse, redirect

# Create your views here.

def index(request):
    context = {'name':"parth", "place":"moradabad"}
    return  render(request, "index.html", context)


def analyze(request):
    # get the text
    text = (request.GET.get("textarea"))

    # check the checkboxes values
    removepunc = (request.GET.get("removepunc", "off"))
    fullcaps = (request.GET.get("fullcaps", "off"))
    newlineremover = (request.GET.get("newlineremover", "off"))
    extraspaceremover = (request.GET.get("extraspaceremover", "off"))

   


    # check which checkbox is on
    if removepunc == "on":
    
        punctuations = '''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''
        analyzed = ""
        for char in text:
            if char not in punctuations:
                analyzed = analyzed+char
    

        params = {'purpose':'removed punctuations', "analysed_text":analyzed}

        # analyze the text
        return render(request, "analyze.html", params)
    

    # checking the uppercase checkbox
    elif (fullcaps=="on"):
        analyzed=""
        for char in text:
            analyzed+=char.upper()
        
        params = {'purpose':'changed to uppercase', "analysed_text":analyzed}

        # analyze the text
        return render(request, "analyze.html", params)
    


    # checking the new Line remover checkbox
    elif (newlineremover=="on"):
        analyzed= ""
        for char in text:
            if char !="\n":
                analyzed+=char
            
        params = {'purpose':'Removed NewLines', "analysed_text":analyzed}
        return render(request, "analyze.html", params)


    # checking the extra space remover checkbox
    elif(extraspaceremover=="on"):
        analyzed = ""
        for index, char in enumerate(text):
            if text[index] == " " and text[index+1] == " ":
                pass

            else:
                analyzed+=char

        params = {'purpose':'Extraspaceremover', "analysed_text":analyzed}
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
