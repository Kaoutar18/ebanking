from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from .models import Page
from .Forms import ContactForm


def index_pages(request, pagename):
    pagename = '/' + pagename
    pg = get_object_or_404(Page, permalink=pagename)
    context = {
        'title': pg.title,
        'content': pg.bodytext,
        'last_updated': pg.update_date,
        'page_list': Page.objects.all(),
               }
    return render(request, 'pages/page.html', context)

def contact(request):
    submitted = False
    if request.method == 'POST':
        form = ContactForm(request.POST, request.FILES)
        if form.is_valid():
            # Traitement du formulaire ici
            form.save()
            return HttpResponseRedirect('/contact/?submitted=True')
    else:
        form = ContactForm()

    return render(request, 'pages/contact.html', {'form': form, 'submitted': submitted})

