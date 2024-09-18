from django.shortcuts import render
from django.http import HttpResponseRedirect

from .ModelForm import QuoteForm

def contact(request):
    return render(request, 'contact.html')
def quote_req(request):
    submitted = False
    if request.method == 'POST':
        form = QuoteForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/quote/?submitted=True')
    else:
        form = QuoteForm()
    return render(request, 'quote.html', {'form': form, 'submitted': submitted})


