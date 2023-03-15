from django.views.decorators.csrf import csrf_exempt
import json
from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from Logica import test

# Create your views here.
''' def index(request):
    return HttpResponse("Hola mundo") '''

# JsonResponse
# def index(request):
#     return JsonResponse({"test":"hola"})


@csrf_exempt
def index(request):
    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)
    try:
        nick_name = body['nick_name']
        full_name = body['full_name']
        created = test.create_user(nick_name, full_name)
        response = {
            "status": "sucessfull",
            "code": 200,
            "data": created
        }
    except Exception as error:
        response = {
            "status": "error",
            "code": 500,
            "data": str(error)
        }
    return JsonResponse(response)


def post(self, request):
    jd = json.loads(request.body)
