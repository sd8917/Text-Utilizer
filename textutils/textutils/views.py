#I have created this file - sudhanshu
from  django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def analyse(request):

    #Get the text
    djtext = request.POST.get('text', 'default')
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')

    print(removepunc)
    print(djtext)

    if removepunc == "on":
        punctuations = '''!@#$%^&*()::"'/,.<>?{}[]'''
        analysed = ""
        for char in djtext:
            if char not in punctuations:
                analysed = analysed + char
        params = {'purpose': 'Removed Punctuations', 'analysed_text': analysed}


    #Analyze the text
        return render(request, 'analyse.html', params)

    elif(fullcaps == 'on'):
        analysed = ""
        for char in djtext:
            analysed = analysed + char.upper()
        params = {'purpose': 'Change to upper case', 'analysed_text': analysed}
        return render(request,  'analyse.html', params)

    elif ( newlineremover == 'on'):
        analysed = ""
        for char in djtext:
            if char != "\n" and char !="\r":
                analysed = analysed + char.upper()
        params = {'purpose': 'Removed new line', 'analysed_text': analysed}
        return render(request, 'analyse.html', params)

    elif (extraspaceremover == 'on'):
        analysed = ""
        for index , char in enumerate(djtext):
            if djtext[index] == " " and djtext[index + 1] == " ":
                pass
            else:
                analysed = analysed + char
        params = {'purpose': 'Remove ths Extra Spaces', 'analysed_text': analysed}
        return render(request, 'analyse.html', params)
    else:
        return HttpResponse("Error")


# def capitalizefirst(request):
#     return HttpResponse('Hello capitalizefirst')
#
# def newlineremove(request):
#     return HttpResponse('Hello newlineremove')
#
# def spaceremove(request):
#     return HttpResponse('Hello spaceremove')
#
# def charcount(request):
#     return HttpResponse('Hello charcount')
