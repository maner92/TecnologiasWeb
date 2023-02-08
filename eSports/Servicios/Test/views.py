from django.shortcuts import render
# from django.http import HttpResponse
from django.http import JsonResponse
from Logica import test

# Create your views here.
''' def index(request):
    return HttpResponse("Hola mundo") '''

#JsonResponse
# def index(request):
#     return JsonResponse({"test":"hola"})

def index(request):
    return JsonResponse({"test": test.f()})