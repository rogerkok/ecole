from django.db import models
class Eleve(models.Model):
    #user = models.OneToOneField('auth.User', related_name='enseignant')

    nom = models.CharField(max_length=256)
    prenom = models.CharField(max_length=256)
    sexe = models.CharField(choices=(('Masculin', 'Masculin'), ('Féminin', 'Féminin')), max_length=256, null=True)
    STATUT = (('Nouveau', 'Nouveau'),
             ('Nouvelle', 'Nouvelle'),
             ('Redoublant', 'Redoublant'),
             ('Redoublante', 'Redoublante'))
    statut = models.CharField(choices=STATUT, max_length=256, null=True)
    classe= models.ForeignKey('etablissements.Classe', related_name='eleves',
                            on_delete=models.CASCADE, null=True)
    #nationalite = CountryField(blank=True, null=True)
    #adresse = models.TextField(blank=True, null=True)
    #contact = models.CharField(max_length=256, blank=True, null=True)
    date_creation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.id.__str__() + " " + self.nom.upper() + " " + self.prenom + " " + self.grade

    class Meta:
        db_table = "eleve"
        verbose_name = "Elève"
        verbose_name_plural = "Elèves"
