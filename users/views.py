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
from statuscode import *
# view for registering users
class RegisterView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

def DuplicateCheck(request):
    try:
        if request.method == 'POST':
            # email = request.POST.get['email']
            data   = json.loads(request.body)
            email = data.get('email', None)
            #email=UserData.objects.get(email = email)
            email=UserData.objects.filter(email = email).first()
    
            if email:
                return JsonResponse(NOEMAIL)

            else:
                return JsonResponse(SUCCESS)

    except Exception as e :
            return JsonResponse({"error":str(e)})

def NameCheck(request):
    try:
        if request.method == 'POST':
            # email = request.POST.get['email']
            data   = json.loads(request.body)
            name = data.get('name', None)
            #email=UserData.objects.get(email = email)
            name=UserData.objects.filter(name = name).first()
    
            if name:
                return JsonResponse(NONAME)

            else:
                return JsonResponse(SUCCESS)

    except Exception as e :
            return JsonResponse({"error":str(e)})


from .serializers import CustomTokenObtainPairSerializer

from .serializers import CustomTokenRefreshSerializer

from rest_framework_simplejwt.views import TokenObtainPairView
class CustomTokenObtainPairView(TokenObtainPairView):
    # Replace the serializer with your custom

    serializer_class = CustomTokenObtainPairSerializer

from rest_framework_simplejwt.views import TokenRefreshView 
class CustomTokenRefreshView(TokenRefreshView):
    serializer_class = CustomTokenRefreshSerializer