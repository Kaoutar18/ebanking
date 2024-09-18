from django.db import models

class Etudiant(models.Model):
    matricule = models.CharField(max_length=10)
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    genre = models.CharField(max_length=1)
    note = models.FloatField()

    def nom_complet(self):
        return f"{self.nom} {self.prenom}"

    def genre_entier(self):
        if self.genre == "M":
            return "Masculin"
        else:
            return "Feminin"

    def mention(self):

            if self.note is not None:
                if self.note >= 16:
                    return "Très bien"
                elif self.note >= 14:
                    return "Bien"
                elif self.note >= 12:
                    return "Assez bien"
                elif self.note >= 10:
                    return "Passable"
                else:
                    return "Non Admis"
            else:
                return "Non Admis"

    def __str__(self):
        return f"Matricule: {self.matricule}, Nom Complet: {self.nom_complet()}, Genre: {self.genre_entier()}, Note: {self.note}"


