from rest_framework import serializers
from .models import *


class Signserializer(serializers.ModelSerializer):

    class Meta:
        model = SignWord  # 가져올 모델명
        # 아래 2옵션 중 택 1
        fields = ["word", "context", "photo_url"] 

class Randomserializer(serializers.ModelSerializer):

    class Meta:
        model = SignWord  # 가져올 모델명
        # 아래 2옵션 중 택 1
        fields = ["sign_id", "word", "photo_url"] 

class Answerserializer(serializers.ModelSerializer):

    class Meta:
        model = SignWord  # 가져올 모델명
        # 아래 2옵션 중 택 1
        fields = ["sign_id", "word"] 