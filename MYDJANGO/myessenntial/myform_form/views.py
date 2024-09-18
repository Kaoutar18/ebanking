from django.shortcuts import render
from django.http import HttpResponse
from .forms import SignupForm, SignupFormWidget, SignupFormData
from django.http import HttpResponseRedirect


def signup10_affichage(request):
    form = SignupForm()
    return render(request, "myform_form/signup10_affichage.html", context={"form": form})


def signup20_widget(request):
    form = SignupFormWidget()
    return render(request, "myform_form/signup20_widget.html", context={"form": form})


def signup30_data(request):
    form = SignupFormData(request.POST)
    if request.method == "POST":
        form = SignupFormData(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            print(cd)
            return HttpResponseRedirect("/myform_form/signup30_reussi/")
    else:
        form = SignupFormData()

    return render(request, "myform_form/signup30_data.html", context={"form": form})


def signup30_reussi(request):
    return render(request, 'myform_form/signup30_reussi.html')


def signup31_data(request):
    form = SignupFormData()
    return render(request, "myform_form/signup31_data.html", context={"form": form})


def signup31_affichage(request):
    form = SignupFormData(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        print(cd)
        return render(request, 'myform_form/signup31_affichage.html', {"cd": cd})
    else:
        return HttpResponse("'Les données ne sont pas valides")