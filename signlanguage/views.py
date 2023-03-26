# backend/signlanguage/views.py
from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.views import View
import json
from rest_framework.views import APIView
from .models import *
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
            id = request.POST['id']
            wordtype = request.POST['wordtype']
            context = request.POST['context']

        url = "http://"+AWS_STORAGE_BUCKET_NAME+".s3.ap-northeast-2.amazonaws.com/" + id+ "." + type
        s3_client.put_object(Body=files, Bucket=AWS_STORAGE_BUCKET_NAME, Key=id+"." + type)

        SignWord.objects.create(word=id,wordtype=wordtype,context=context,photo_url=url)
    
        return JsonResponse({"url" : url})

    except Exception as e :
            print(e)
            return JsonResponse({"ERROR" : "e.message"})