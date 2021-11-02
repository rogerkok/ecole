from django.db import models
from django_countries.fields import CountryField
from phone_field import PhoneField

# Create your models here.
class AnneeScolaire(models.Model):
    nom = models.CharField(max_length=11)
    date_creation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nom
    class Meta:
        db_table = "annee_scolaire"
        verbose_name = "Année scolaire"
        verbose_name_plural = "Années scolaires"


class Decoupage(models.Model):
    nom = models.CharField(max_length=256)
    type = models.CharField(blank=True, null=True, choices=(('trimestriel', 'Trimestriel'), ('semestriel', 'Semestriel')), max_length=256)
    periode = models.CharField(max_length=256)
    anneescolaire = models.ForeignKey('etablissements.AnneeScolaire', related_name='decoupages', on_delete=models.CASCADE, null=True)
    date_creation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nom
    class Meta:
        db_table = "decoupage"
        verbose_name = "Découpage"
        verbose_name_plural = "Découpages"

class Dre(models.Model):
    nom = models.CharField(max_length=256)
    rep = models.CharField(blank=True, null=True, max_length=256)
    adresse = models.TextField(blank=True, null=True)
    pays= CountryField(blank=True, null=True, help_text='Pays')
    contact = models.BigIntegerField(blank=True, null=True)
    email = models.EmailField(blank=True, null=True, max_length=50)
    date_creation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nom
    class Meta:
        db_table = "dre"
        verbose_name = "Direction Régionnale"
        verbose_name_plural = "Directions Régionnales"

class Inspection(models.Model):
    nom = models.CharField(max_length=256)
    adresse = models.TextField(blank=True, null=True)
    contact = models.BigIntegerField(blank=True, null=True)
    email = models.EmailField(blank=True, null=True, max_length=50)
    dre = models.ForeignKey('etablissements.Dre', related_name='inspections',
                                      on_delete=models.CASCADE, null=True)
    date_creation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nom
    class Meta:
        db_table = "inspection"
        verbose_name = "Inspection"
        verbose_name_plural = "Inspections"

class Etablissement(models.Model):
    nom = models.CharField(max_length=256)
    adresse = models.TextField(blank=True, null=True)
    contact = models.BigIntegerField(blank=True, null=True)
    email = models.EmailField(blank=True, null=True, max_length=50)
    dre = models.ForeignKey('etablissements.Inspection', related_name='etablissements',
                                      on_delete=models.CASCADE, null=True)
    chef = models.OneToOneField('etablissements.Enseignant', related_name='chefetb',on_delete=models.CASCADE, null=True)
    date_creation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nom
    class Meta:
        db_table = "etablissement"
        verbose_name = "Etablissement"
        verbose_name_plural = "Etablissements"

class Enseignant(models.Model):
    #user = models.OneToOneField('auth.User', related_name='enseignant')

    nom = models.CharField(max_length=256)
    prenom = models.CharField(max_length=256)
    sexe = models.CharField(choices=(('Masculin', 'Masculin'), ('Féminin', 'Féminin')), max_length=256)
    GRADE = (('PR', 'Professeur'),
             ('MCA', 'Maitre de conference A'),
             ('MCB', 'Maitre de conference B'),
             ('MAA', 'Maitre assistant A'),
             ('MAB', 'Maitre assistant B'),
             ('DR', 'Docteur'),
             ('M', 'Master'),
             ('M1', 'Master I'),
             ('L', 'Licence'))
    grade = models.CharField(choices=GRADE, max_length=256)
    etbs = models.ForeignKey('etablissements.Etablissement', related_name='enseignants', on_delete=models.CASCADE, null=True)
    nationalite = CountryField(blank=True, null=True)
    adresse = models.TextField(blank=True, null=True)
    contact = models.CharField(max_length=40, blank=True, null=True)
    date_creation = models.DateTimeField(auto_now_add=True)
    photo = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.id.__str__() + " " + self.nom.upper() + " " + self.prenom + " " + self.grade

    class Meta:
        db_table = "enseignant"
        verbose_name = "Enseignant"
        verbose_name_plural = "Enseignants"

class Classe(models.Model):
    #user = models.OneToOneField('auth.User', related_name='enseignant')

    nom = models.CharField(max_length=256)
    SERIE = (('A4', 'A4'),
             ('S', 'S'),
             ('D', 'D'),
             ('C4', 'C'),
             ('E', 'E'),
             ('F2', 'F2'),
             ('F4', 'F4'),
             ('G1', 'G1'),
             ('G2', 'G2'),
             ('G3', 'G3'))
    serie = models.CharField(choices=SERIE, max_length=256)
    etbs = models.ForeignKey('etablissements.Etablissement', related_name='classes',
                            on_delete=models.CASCADE, null=True)
    date_creation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.id.__str__() + " " + self.nom.upper() + " " + self.serie

    class Meta:
        db_table = "classe"
        verbose_name = "Classe"
        verbose_name_plural = "Classes"

class Matiere(models.Model):
    #user = models.OneToOneField('auth.User', related_name='enseignant')

    nom = models.CharField(max_length=256)

    date_creation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.id.__str__() + " " + self.nom.upper()

    class Meta:
        db_table = "matiere"
        verbose_name = "Matière"
        verbose_name_plural = "Matières"
class MatiereClasse(models.Model):
    #user = models.OneToOneField('auth.User', related_name='enseignant')
    classe = models.ForeignKey('etablissements.Classe', related_name='matieres',
                             on_delete=models.CASCADE, null=True)
    matiere = models.ForeignKey('etablissements.Matiere', related_name='matieres',
                               on_delete=models.CASCADE, null=True)
    enseigant = models.ForeignKey('etablissements.Enseignant', related_name='matieres',
                             on_delete=models.CASCADE, null=True)

    coef = models.IntegerField(default=1)


    date_creation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.id.__str__() + " " + self.nom.upper()

    class Meta:
        db_table = "matiere_classe"
        verbose_name = "Matière de la classe"
        verbose_name_plural = "Matières de la classe"