from rest_framework import serializers
from .models import UserData
import json
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.http import JsonResponse
from statuscode import *
class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserData
        fields = [ "email", "name", "password"]

    def create(self, validated_data):
        user = UserData.objects.create(email=validated_data['email'],
                                       name=validated_data['name']
                                         )
        user.set_password(validated_data['password'])
        user.save()
        return user

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
    
        od1 = json.dumps(attrs)
        od2 = json.loads(od1)

        
        name=UserData.objects.filter(email = od2['email']).first()

        if name:
            if not name.check_password(od2['password']) :

                data1=VAILDPASSWORD
                return data1

            else:
                data1="success"
      
        else:
            
            data1= VAILDEMAIL
            return data1

        data = super(CustomTokenObtainPairSerializer, self).validate(attrs)
       
        return data