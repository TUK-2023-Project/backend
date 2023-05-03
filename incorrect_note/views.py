from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.
from .models import *
def printdd(request):
    if request.method == 'GET':
        print("dd")
        Incorret.objects.create(user_id=Userdata.id, sign_id="1")
        return JsonResponse({"url" : "D"})