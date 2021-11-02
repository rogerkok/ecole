from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from etablissements.models import *
from etablissements.serializers import AnneeScolaireSerializer, MatiereSerializer,EnseignantSerializer
from django.http.response import JsonResponse
from django.core.files.storage import default_storage
# Create your views here.
@csrf_exempt
def anneeApi(request,id=0):
    if request.method=='GET':
        annees = AnneeScolaire.objects.all()
        annees_serializer = AnneeScolaireSerializer(annees, many=True)
        return JsonResponse(annees_serializer.data, safe=False)
    elif request.method=='POST':
        annee_data=JSONParser().parse(request)
        annee_serializer = AnneeScolaireSerializer(data=annee_data)
        if annee_serializer.is_valid():
            annee_serializer.save()
            return JsonResponse("Année ajoutée avec succès", safe=False)
        return JsonResponse("Echec", safe=False)
    elif request.method=='PUT':
        annee_data=JSONParser().parse(request)
        annee = AnneeScolaire.objects.get(id=annee_data['id'])
        annee_serializer = AnneeScolaireSerializer(annee, data=annee_data)
        if annee_serializer.is_valid():
            annee_serializer.save()
            return JsonResponse("Mise à jour avec succès", safe=False)
        return JsonResponse("Echec", safe=False)
    elif request.method=='DELETE':
        annee = AnneeScolaire.objects.get(id=id)
        annee.delete()
        return JsonResponse("Suppression avec succès", safe=False)
@csrf_exempt
def matiereApi(request,id=0):
    if request.method=='GET':
        matieres = Matiere.objects.all()
        matieres_serializer = MatiereSerializer( matieres, many=True)
        return JsonResponse( matieres_serializer.data, safe=False)
    elif request.method=='POST':
        matiere_data=JSONParser().parse(request)
        matiere_serializer = MatiereSerializer(data= matiere_data)
        if  matiere_serializer.is_valid():
            matiere_serializer.save()
            return JsonResponse("Matière ajoutée avec succès", safe=False)
        return JsonResponse("Echec", safe=False)
    elif request.method=='PUT':
        matiere_data=JSONParser().parse(request)
        matiere = Matiere.objects.get(id= matiere_data['id'])
        matiere_serializer = MatiereSerializer( matiere, data= matiere_data)
        if  matiere_serializer.is_valid():
            matiere_serializer.save()
            return JsonResponse("Mise à jour avec succès", safe=False)
        return JsonResponse("Echec", safe=False)
    elif request.method=='DELETE':
        matiere =Matiere.objects.get(id=id)
        matiere.delete()
        return JsonResponse("Suppression avec succès", safe=False)
@csrf_exempt
def ensApi(request,id=0):
    if request.method=='GET':
        enseignants = Enseignant.objects.all()
        enseignants_serializer =EnseignantSerializer(enseignants, many=True)
        return JsonResponse( enseignants_serializer.data, safe=False)
    elif request.method=='POST':
        enseignant_data=JSONParser().parse(request)
        enseignant_serializer = EnseignantSerializer(data= enseignant_data)
        if enseignant_serializer.is_valid():
            enseignant_serializer.save()
            return JsonResponse("Enseignant ajoutée avec succès", safe=False)
        return JsonResponse("Echec", safe=False)
    elif request.method=='PUT':
        enseignant_data=JSONParser().parse(request)
        enseignant = Enseignant.objects.get(id= enseignant_data['id'])
        enseignant_serializer = EnseignantSerializer( enseignant, data= enseignant_data)
        if  enseignant_serializer.is_valid():
            enseignant_serializer.save()
            return JsonResponse("Mise à jour avec succès", safe=False)
        return JsonResponse("Echec", safe=False)
    elif request.method=='DELETE':
        enseignant =Enseignant.objects.get(id=id)
        enseignant.delete()
        return JsonResponse("Suppression avec succès", safe=False)
@csrf_exempt
def savefile(request):
    file= request.FILES['uploadFile']
    file_name = default_storage.save(file.name,file)
    return JsonResponse(file_name, safe=False)