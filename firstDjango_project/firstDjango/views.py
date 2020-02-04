from django.http import HttpResponse
from django.shortcuts import render

def home(request): # from url page it recieve request
    #return HttpResponse('This is our home page')
    return render(request,'home.html',{'author':'Imad Nazim','date':'27/12/19'})  # will sent request from urls to home.html  # give template path in settings.py -> templates -> DIRS
#render(request, template_name, context=None(dictionary), content_type=None, status=None, using=None)

def gate(request):
    return HttpResponse('<h3>This is our gate page</h3 >')

import collections
from operator import itemgetter
def count(request):
    ft=request.GET['fulltext']  #recieve from url of home
    print(type(ft))   # string
    wordlist=ft.split()
    wdict=collections.Counter(wordlist)
    # wdict=wdict.sort(key=itemgetter(1),reverse=True)

    return render(request,'count.html',{'text':ft,'nwords':len(wordlist),'worddictionary':wdict,'mostcommon':wdict.most_common(2)})

def about(request):
    return render(request,'about.html')
