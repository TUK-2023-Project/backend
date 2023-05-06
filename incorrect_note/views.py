from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
import jwt
from utils import *
# Create your views here.
from .models import *
from statuscode import *

@api_view(['GET'])
def add_note(request):
    # if request.method == 'GET':
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
        sign_id=SignWord.objects.get(sign_id=sign_id)

        Incorret.objects.create(user_id=id, sign_id=sign_id)

        return Response(SUCCESS,status=status.HTTP_200_OK)

        #추가하는 값이 is deleted가 false인데 다시 값 있으면 
        #Item.objects.filter(create_dt__year=2020).update(available=False)
        #만약에 db에 지워졌는데 ㅣㅇㅆ으면 유저랑 사인 아이디의 값이 이미 존재하는 필드라면 is deleted를 바꾸고 
        #아니라면 else로 위 코드 실행 한다.

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
        
        sign_id = request.GET.get('sign_id', None)
        id=UserData.objects.get(id=user_id)
        sign_id=SignWord.objects.get(sign_id=sign_id)
        Incorret.objects.filter(user_id=id, sign_id=sign_id).update(is_deleted=True)
        return Response(SUCCESS,status=status.HTTP_200_OK)