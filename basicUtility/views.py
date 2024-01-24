
# Created by kalpesh
from django.http import HttpResponse
from django.shortcuts import render, redirect
import string

def index(request):
    return render(request, 'index.html')

def analyzed(request):
    getText = request.GET.get("Text", "")
    firstCap = request.GET.get("Capitalize", "off")
    upper = request.GET.get("Uppercase", "off")
    lower = request.GET.get("lowercase", "off") 
    removepunc = request.GET.get("removepunc", "off") 
    remNewLine = request.GET.get("remNewLine", "off") 
    remSpace = request.GET.get("remSpace", "off") 
    remExtraSpace = request.GET.get("remExtraSpace", "off") 
    charCount = request.GET.get("charCount", "off") 

    if (firstCap == "on"):
        analyzed = ""
        analyzed = getText.capitalize()

        param = {"analyzed" : analyzed}
        return render(request, 'index.html', param)

    elif(upper == "on"):
        analyzed = ""
        analyzed = analyzed + getText.upper()

        param = {"analyzed" : analyzed}
        return render(request, 'index.html', param)    

    elif(lower == "on"):
        analyzed = ""
        analyzed = analyzed + getText.lower()

        param = {"analyzed" : analyzed}
        return render(request, 'index.html', param)    

    elif(removepunc == "on"):
        analyzed = ""
        for char in getText:
            if char not in string.punctuation:
                analyzed = analyzed + char

        param = {"analyzed" : analyzed}
        return render(request, 'index.html', param) 

    elif(remNewLine == "on"):
        analyzed = " "
        for char in getText:
            if char != "\n":
                analyzed = analyzed + char

        param = {"analyzed" : analyzed}
        return render(request, 'index.html', param) 

        
    elif(remSpace == "on"):
        analyzed = " "
        for char in getText:
            if char != " ":
                analyzed = analyzed + char

        param = {"analyzed" : analyzed}
        return render(request, 'index.html', param) 

    elif(remExtraSpace == "on"):
        analyzed = " "
        for index, char in enumerate(getText):
            if not (getText[index] == " " and getText[index + 1] == " "):
                analyzed = analyzed + char

        param = {"analyzed" : analyzed}
        return render(request, 'index.html', param) 
     
    elif(charCount == "on"):
        analyzed = " "
        for char in getText:
            if char in string.ascii_letters:
                analyzed = analyzed + char


        param = {"analyzed" : len(analyzed)}
        return render(request, 'index.html', param) 
     
    else:

        return HttpResponse("Error")    

def about(request):
    return render(request, 'about.html')


def calculator(request):
    return render(request, 'calculator.html')

def conversion(request):
    return render(request, 'Conversion.html')

def convert(request):
    getNumber = int(request.GET.get("number", ""))
    binary = request.GET.get("binary", "off")
    octal = request.GET.get("octal", "off")
    hexa = request.GET.get("hexadecimal", "off")
    conv = ""
    if (binary == "on"):
        conv = bin(getNumber).replace("0b", "")
        param = {"conversion": "Binary","converted": conv}

        return render(request, 'Conversion.html', param)

    elif (octal == "on"):
        conv = oct(getNumber).replace("0o", "")
        param = {"conversion": "Octal","converted": conv}

        return render(request, 'Conversion.html', param)
    
    elif (hexa == "on"):
        conv = hex(getNumber).replace("0x", "")
        param = {"conversion": "Hexadecimal","converted": conv}

        return render(request, 'Conversion.html', param)
    