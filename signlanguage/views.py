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
# sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))))
# from users import models

def receive_video(request):
    if request.method == "POST":
        video_data = request.body
        # Do some processing with the video data
        cumulative_video_size = ...
        # ...
        return JsonResponse({"cumulative_video_size": cumulative_video_size})
    return JsonResponse({"error": "Invalid request method"})

import boto3
from backend.settings import AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, AWS_STORAGE_BUCKET_NAME

def get_file_url(request):
    try:
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
            print(e)
            return JsonResponse({"ERROR" : "e.message"})

def get_info(request):
    #틀린 문제 오답노트에 저장
    if request.method == 'POST':
        word = request.POST['word']
        a=SignWord.objects.filter(word = word).values_list("context", "photo_url")

        return a

import random
def three_random(request):

    if request.method == 'POST':
        wordinput=[]
        word = request.POST['wordtype']
        date = request.POST.getlist('input[]')

        #테스트 할때 미리 db에 수어정보 업로드 시켜서 테스트 해야함 
        # J=['1','2','3','4','5'] #자음
        # M=['1','2','3','4','5'] #모음
        # A=['1','2','3','4','5'] #알파벳

        J=['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19'] #자음
        M=['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21'] #모음
        A=['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26']#알파벳

        if(word=='1'): #추후enum으로 변경예정
    
            wordinput=J
            print(wordinput)
        elif(word=='2'):
            wordinput=M
            print(wordinput)

        elif(word=='3'):
            wordinput=A
            print(wordinput)
        else:
            print("else")


        for i in date:
   
            wordinput.remove(i)
   

        three_word=random.sample(wordinput,3)


        first = SignWord.objects.get(sign_id=three_word[0])
    
        second = SignWord.objects.get(sign_id=three_word[1])
        third = SignWord.objects.get(sign_id=three_word[2])

        answerone=random.sample(three_word,1)
        answer = SignWord.objects.get(sign_id=answerone[0])

    return JsonResponse({"questions" : [
        {"id":first.sign_id, "word": first.word,"photo_url":first.photo_url},
        {"id":second.sign_id, "word": second.word,"photo_url":second.photo_url},
        {"id":third.sign_id, "word": third.word,"photo_url":third.photo_url},
    
    ],
    "answer":{
        "id":answer.sign_id,
        "word":answer.word
    }
    })
