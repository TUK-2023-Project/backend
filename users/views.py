# from django.shortcuts import render

# Create your views here.
from django.contrib.auth.forms import UserCreationForm
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .models import *

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

# import jwt
# from rest_framework_simplejwt.tokens import AccessToken
# token_str ="eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjc5ODE4OTgzLCJpYXQiOjE2Nzk4MTE3ODMsImp0aSI6IjdmODYwM2E5YjNiZjQ4NDJhZGEzZThhNzcwNDAyMDU1IiwidXNlcl9pZCI6M30.oqVdmhLkmL0ByXd-clb-xNetfaMvahylnd7IHRek0dY"
# access_token = AccessToken(token_str)
# user1 = UserData.objects.get(id=access_token['user_id'])
# print(user1)


        # print("-------------------")
        # print("3333333333333333333333333")