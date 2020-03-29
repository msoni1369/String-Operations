from django.shortcuts import render

def index(request):    
    return render(request,'index.html' )


def analyze(request):
    #Get the text
    django_text = request.POST.get('text','default')

    #check checkboxes values
    removepunc = request.POST.get('removepunc','off')
    fullcaps = request.POST.get('fullcaps','off')
    newline = request.POST.get('newlineremover', 'off')
    spaceremover = request.POST.get('spaceremover', 'off')
    charcount = request.POST.get('charcount', 'off')
   
    #initializing dictionary
    params = { 'purpose' : '' , 'analyzed_text' : django_text }
    
    #check which checkboxes is on
    if removepunc == "on":
        analyzed = ""
        punctuations = '''!()-[]{};:'"\|,<>./?@#$%^*&_~`'''
        for char in django_text:
            if char not in punctuations:
                analyzed = analyzed + char
        params = { 'purpose' : 'Changed to Remove Punctuations' , 'analyzed_text' : analyzed }
        django_text = analyzed                        
    
    if(fullcaps == 'on'):
        analyzed = ""  
        for char in django_text:
            analyzed = django_text.upper()
        params = { 'purpose' : 'Changed to UPPERCASE' , 'analyzed_text' : analyzed }
        django_text = analyzed

    if(newline == 'on'):
        analyzed = ""
        for char in django_text:
            if (char != '\n' and char != '\r'):
                analyzed = analyzed + char
        params = { 'purpose' : 'Changed to New Line Remover' , 'analyzed_text' : analyzed }
        django_text = analyzed   

    if(spaceremover == 'on'):
        analyzed = ""
        for char in django_text:
            if char != ' ' :
                analyzed = analyzed + char
        params = { 'purpose' : 'Changed to Space Remover' , 'analyzed_text' : analyzed }
        django_text = analyzed

    if(charcount == 'on'):
        count = 0
        for char in django_text:
            if char != ' ' and char != "\n" and char != "\r":
                count = count + 1
        params = { 'purpose' : 'Changed to Character Count' , 'analyzed_text' :  "characters present in this "+django_text+" is "+str(count) }
    
    if (removepunc=="on" or spaceremover=="on" or newline=="on" or charcount=="on" or fullcaps=="on"):
        return render(request,'analyze.html',params)

    #if none of the checkboxes checked
    if not(removepunc=="on" and spaceremover=="on" and newline=="on" and charcount=="on" and fullcaps=="on"):       
        return render(request,'not_analyze.html',params)
