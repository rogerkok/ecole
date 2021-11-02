from django.contrib import admin
from .models import *
class AnneeAdmin(admin.ModelAdmin):
    pass
admin.site.register(AnneeScolaire, AnneeAdmin)
admin.site.register(Decoupage, AnneeAdmin)
admin.site.register(Dre, AnneeAdmin)
admin.site.register(Inspection, AnneeAdmin)
admin.site.register(Etablissement, AnneeAdmin)
admin.site.register(Enseignant, AnneeAdmin)
admin.site.register(Classe, AnneeAdmin)
admin.site.register(Matiere, AnneeAdmin)
admin.site.register(MatiereClasse, AnneeAdmin)
