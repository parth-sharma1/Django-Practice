from django.shortcuts import render, HttpResponse, redirect

# Create your views here.

def index(request):
    context = {'name':"parth", "place":"moradabad"}
    return  render(request, "index.html", context)


def analyze(request):
    # get the text
    text = (request.POST.get("text"))

    # check the checkboxes values
    removepunc = (request.POST.get("removepunc", "off"))
    fullcaps = (request.POST.get("fullcaps", "off"))
    newlineremover = (request.POST.get("newlineremover", "off"))
    extraspaceremover = (request.POST.get("extraspaceremover", "off"))
    charcount = (request.POST.get("charcount", "off"))

   


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
            if char !="\n" and char !="\r":
                analyzed+=char
            
        params = {'purpose':'Removed NewLines', "analysed_text":analyzed}
        return render(request, "analyze.html", params)


    # checking the extra space remover checkbox
    elif(extraspaceremover=="on"):
        analyzed = " ".join(text.split())


        params = {'purpose': 'Removed Extra Spaces', 'analysed_text': analyzed}
        return render(request, "analyze.html", params)
    

        # analyzed = ""
        # for index, char in enumerate(text):
        #     if text[index] == " " and text[index+1] == " ":
        #         pass

        #     else:
        #         analyzed+=char

        # params = {'purpose':'Extra Space Remover', "analysed_text":analyzed}
        # return render(request, "analyze.html", params)




    # checking charcount condition
    elif (charcount=="on"):

 
        count = 0
        for char in text:
            if char != " ":
          
                count+=1
        analyzed= f" This text has {count} number of Characters.."
   
        
        params = {'purpose':'character count', "analysed_text": analyzed}
        return render (request, "analyze.html", params )
    # f"this text has {count} character"
       
       
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
