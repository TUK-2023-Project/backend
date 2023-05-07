from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
import jwt
from utils import *
from .serializers import *
from .models import *
from statuscode import *

@api_view(['GET'])
def add_note(request):
    # if request.method == 'GET':
    try:
        token = request.META.get('HTTP_ACCESS', None)
        if token is None:

            return Response(TOKEN_ERROR,status=status.HTTP_404_NOT_FOUND)

        try:
            user_id = get_user_id_from_token(token.split(' ')[1])

        except jwt.exceptions.ExpiredSignatureError:
            return Response(TOKEN_EXPIRE, status=status.HTTP_401_UNAUTHORIZED)

        except jwt.exceptions.DecodeError:
            return Response(TOKEN_VAILD, status=status.HTTP_401_UNAUTHORIZED)
        
        sign_id = request.GET.get('sign_id', None)
        id=UserData.objects.get(id=user_id)

        if(SignWord.objects.filter(sign_id=sign_id)):
            sign_id=SignWord.objects.get(sign_id=sign_id)
        else:
            raise Exception('signword에 없는 값입니다.')
       
        if(Incorret.objects.filter(user_id=id, sign_id=sign_id)):
            Incorret.objects.filter(user_id=id, sign_id=sign_id).update(is_deleted=False)
        
        else:
            Incorret.objects.create(user_id=id, sign_id=sign_id)
        return Response(SUCCESS,status=status.HTTP_200_OK)
    
    except Exception as e:                            
        print(e)

        

@api_view(['GET'])
def delete_note(request):

        token = request.META.get('HTTP_ACCESS', None)
        if token is None:
            return Response(TOKEN_ERROR,status=status.HTTP_404_NOT_FOUND)

        try:
            user_id = get_user_id_from_token(token.split(' ')[1])

        except jwt.exceptions.ExpiredSignatureError:
            return Response(TOKEN_EXPIRE, status=status.HTTP_401_UNAUTHORIZED)

        except jwt.exceptions.DecodeError:
            return Response(TOKEN_VAILD, status=status.HTTP_401_UNAUTHORIZED)
        
        try:
            sign_id = request.GET.get('sign_id', None)
            id=UserData.objects.get(id=user_id)
            sign_id=SignWord.objects.get(sign_id=sign_id)
            Incorret.objects.filter(user_id=id, sign_id=sign_id).update(is_deleted=True)
            return Response(SUCCESS,status=status.HTTP_200_OK)
        except Exception as e:                           
            print(e) 


@api_view(['GET'])
def show_list_note(request):
        token = request.META.get('HTTP_ACCESS', None)
        if token is None:
            return Response(TOKEN_ERROR,status=status.HTTP_404_NOT_FOUND)

        try:
            user_id = get_user_id_from_token(token.split(' ')[1])

        except jwt.exceptions.ExpiredSignatureError:
            return Response(TOKEN_EXPIRE, status=status.HTTP_401_UNAUTHORIZED)

        except jwt.exceptions.DecodeError:
            return Response(TOKEN_VAILD, status=status.HTTP_401_UNAUTHORIZED)
        try:
            response_data = []

            id=UserData.objects.get(id=user_id)
            sign_list = Incorret.objects.filter(user_id=id,is_deleted=False).values("sign_id")

            for i in sign_list:
                string=str(i["sign_id"])
                response_data.append(string)

            response_data2 = []

            for i in response_data:
                count=0
                a=SignWord.objects.get(sign_id=i[count])
                count=count+1
                response_data2.append(Listserializer(a).data)
            
            return JsonResponse({'data_list':response_data2})

        except Exception as e:                         
            print(e)