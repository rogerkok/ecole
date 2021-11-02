from django.contrib import admin

from .models import *
class AnneeAdmin(admin.ModelAdmin):
    pass
admin.site.register(Eleve, AnneeAdmin)
