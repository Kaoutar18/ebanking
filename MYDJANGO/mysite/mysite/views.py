from django.shortcuts import render
from django.http import HttpResponse

from pages.models import Page


def index_projet(request):
    #  return HttpResponse("<h1 style='text-align:center;'>Bienvenue au site de Master GLWA</h1>")
   # return render(request, "base.html")
    page_list = Page.objects.all()
    return render(request, "base.html", {'page_list': page_list})

def contact(request):
    return render(request, 'pages/contact.html')
def quote(request):
    return render(request, 'quotes/quote.html')

