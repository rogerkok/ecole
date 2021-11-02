from django.conf.urls import url
from etablissements import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns=[
    url(r'^annee/$', views.anneeApi),
    url(r'^annee/([0-9]+)$', views.anneeApi),
    url(r'^matiere/$', views.matiereApi),
    url(r'^matiere/([0-9]+)$', views.matiereApi),
    url(r'^ens/$', views.ensApi),
    url(r'^ens/([0-9]+)$', views.ensApi),
    url(r'^savefile/$', views.savefile)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)