# backend/signlanguage/views.py
from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.views import View
import json
from rest_framework.views import APIView
from .models import *
import os
import sys
from .serializers import *
from rest_framework import status
from rest_framework.response import Response
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))))
from utils import *
import boto3
from backend.settings import AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, AWS_STORAGE_BUCKET_NAME

"""
이름: 박수연
내용: 수어 정보 db에 저장및 s3업로드
날짜:3/30
"""


def get_file_url(request):
    try:
    
        # token = request.META.get('HTTP_ACCESS', None)
        # if token is None:
        #     return JsonResponse({'message': '토큰이 필요합니다'})
        # user_id = get_user_id_from_token(token.split(' ')[1])

        # except AuthenticationFailed as e:

        #     return JsonResponse({'message': str(e)})

        s3_client = boto3.client(
            's3',
            aws_access_key_id=AWS_ACCESS_KEY_ID,
            aws_secret_access_key=AWS_SECRET_ACCESS_KEY
        )
        #word = request.data.get['word']

        type = "jpg"
        files = request.FILES['files']
        
        if request.method == 'POST':

            sign_id = request.POST['sign_id']

            word = request.POST['word']#ex'기역'
            wordtype = request.POST['wordtype'] 
            context = request.POST['context']

        url = "http://"+AWS_STORAGE_BUCKET_NAME+".s3.ap-northeast-2.amazonaws.com/" + sign_id+ "." + type
        s3_client.put_object(Body=files, Bucket=AWS_STORAGE_BUCKET_NAME, Key=sign_id+"." + type)
        SignWord.objects.create(sign_id=sign_id, word=word,wordtype=wordtype,context=context,photo_url=url)
        return JsonResponse({"url" : url})

    except Exception as e :
            return JsonResponse({"error":str(e)})

"""
이름: 박수연
내용: 틀린문제에 관한 내용 반환
날짜:3/30
"""

def get_info(request):
    try:    
            
    # token = request.META.get('HTTP_ACCESS', None)
    # if token is None:
    #     return JsonResponse(TOKEN_ERROR)
    # user_id = get_user_id_from_token(token.split(' ')[1])

        if request.method == 'GET':
            sign_id = request.GET.get('sign_id', None)
            # data   = json.loads(request.body)
            # sign_id = data.get('sign_id', None)

        # sign_id = request.POST['sign_id']
            a=SignWord.objects.get(sign_id = sign_id)
            userserialize = Signserializer(a).data
            return JsonResponse({"sign_language_info"  :userserialize
            
            }     
              )

    except Exception as e :
        return JsonResponse({"error":str(e)})
    
    


"""
이름: 박수연
내용: 랜덤값 반환
날짜:3/30
"""


import random
class SignView(APIView):
    def get(self,request):

        # token = request.META.get('HTTP_ACCESS', None)
        # if token is None:
        #     return JsonResponse({'message': '토큰이 필요합니다'})
        # user_id = get_user_id_from_token(token.split(' ')[1])


        try:
            wordinput=[]
            category_id = request.GET.get('category_id', None)
            date=self.request.query_params.get('solvedlist')
            date=date.split(',')

        
            #테스트 할때 미리 db에 수어정보 업로드 시켜서 테스트 해야함       
            id_list=SignWord.objects.filter(wordtype=category_id).values("sign_id")
            count = id_list.count()
            print(date)
      
            for i in range(count):
               
                wordinput.append( str(id_list[i]["sign_id"]))

     
            wordinputlist = wordinput[:] #wordinputlist에 원본 값 저장
        
            if(len(wordinput)==len(date)):
                print("모든 문제 다 풀었습니다")
                return JsonResponse({"state" : "clear"})
            print(date)

            if(date[0]!="0"):
                for i in date:
                    wordinput.remove(i) #wordinput에 정답 후보들만 남기기
            
            if(len(wordinput)<3):
                three_word=wordinput[:]
  
                for i in random.sample(date,3-len(wordinput)): #맞춘 정답주에서 필요한 만큼만 랜덤값 추출
                    three_word.append(str(i))


            else:
                three_word=random.sample(wordinput,3)


            first = SignWord.objects.get(sign_id=three_word[0])
            firstserialize = Randomserializer(first).data
        
            second = SignWord.objects.get(sign_id=three_word[1])
            secondserialize = Randomserializer(second).data
    
            third = SignWord.objects.get(sign_id=three_word[2])
            thirdserialize = Randomserializer(third).data

            answerone=random.sample(three_word,1)
          
            answer = SignWord.objects.get(sign_id=answerone[0])
        ###문제를 다 풀었을 경우 리턴값을 따로 만들자
        
            return JsonResponse({"questions" : [
                {
                "id":first.sign_id,
                "word":first.word,
                "photo_url":first.photo_url
                },
                    {
                "id":second.sign_id,
                "word":second.word,
                "photo_url":second.photo_url
                },
                    {
                "id":third.sign_id,
                "word":third.word,
                "photo_url":third.photo_url
                },
        
            ],
            "answer":{
                "id":answer.sign_id,
                "word":answer.word
            }
            })
        except Exception as e :
            return JsonResponse({"error":str(e)})


        # return JsonResponse({"questions" : [
        #     firstserialize,
        #     secondserialize,
        #     thirdserialize,

        # ],
        # "answer":Answerserializer
        # })
