# backend/signlanguage/views.py
from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.views import View
import json

def receive_video(request):
    if request.method == "POST":
        video_data = request.body
        # Do some processing with the video data
        cumulative_video_size = ...
        # ...
        return JsonResponse({"cumulative_video_size": cumulative_video_size})
    return JsonResponse({"error": "Invalid request method"})