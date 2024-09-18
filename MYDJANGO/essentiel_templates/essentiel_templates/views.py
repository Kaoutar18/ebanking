import datetime

from django.shortcuts import render
from . models import Etudiant



def index(request):
    return render(request, "index.html")
def view_static(request):
    return render(request, "temp_static.html")
def view_variables(request):
    vint = 10
    vfloat =10.5
    vboolean =True
    vstring="bonjour"
    vdate=datetime.datetime.today()
    dictionnaire={"vint":vint,
                  "vfloat":vfloat,
                  "vboolean":vboolean,
                  "vstring":vstring,
                  "vdate":vdate}
    return render(request, "temp_variables.html", context=dictionnaire)
def view_attributs(request):
    etudiant = Etudiant.objects.create(matricule="Etud001", nom="bahroune", prenom="said", genre="M", note=12.5)

    context = {"etudiant": etudiant}
    return render(request, "temp_attributsObjet.html", context)
def view_alternative(request):
    etudiant = Etudiant.objects.create(matricule="Etud001", nom="Chamsoune", prenom="Meryem", genre="F", note=19.5)

    context = {"etudiant": etudiant}
    return render(request, "temp_alternative.html", context)
def view_boucle(request):
    classe = [
        Etudiant("Etud001", "Bahroune", "Said", "M", 12.5),
        Etudiant("Etud002", "Naimoune", "Ali", "M", 8.5),
        Etudiant("Etud003", "Misbahoume", "Nadia", "F", 15.5),
        Etudiant("Etud004", "Chamsoune", "Meryem", "F", 19.5),
        Etudiant("Etud005", "Mardyoune", "Fouad", "F", 13.5),
        Etudiant("Etud006", "Mouttakioune", "Said", "F", 10.5),
    ]

    s = 0
    for etudiant in classe:
        if etudiant.note is not None:
            s += etudiant.note

    moyenne = round(s / len(classe), 2)
    classe_vide = []  # Ajoutez votre logique pour remplir classe_vide

    context = {"classe": classe, "moyenne": moyenne, "classe_vide": classe_vide}
    return render(request, "temp_boucle.html", context)


