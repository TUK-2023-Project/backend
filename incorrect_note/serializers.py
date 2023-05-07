from rest_framework import serializers
from .models import SignWord

class Listserializer(serializers.ModelSerializer):

    class Meta:
        model = SignWord  # 가져올 모델명
        # 아래 2옵션 중 택 1
        fields = ["sign_id", "word", "wordtype"] 