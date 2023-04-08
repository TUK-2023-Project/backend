# from django.shortcuts import render

# Create your views here.
from django.contrib.auth.forms import UserCreationForm
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .models import *
import json
import bcrypt
from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import UserSerializer
from rest_framework.response import Response

# view for registering users
class RegisterView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

def DuplicateCheck(request):

    if request.method == 'POST':
        # email = request.POST.get['email']
        data   = json.loads(request.body)
        email = data.get('email', None)
        #email=UserData.objects.get(email = email)
        email=UserData.objects.filter(email = email).first()
   
        if email:
             return JsonResponse({"status":400})

        else:
            return JsonResponse({"status":200})
