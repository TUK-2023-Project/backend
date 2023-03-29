# serializers.py 파일은 모델 인스턴스를 JSON 형식으로 변환하는 작업을 수행
from rest_framework import serializers
from .models import Rank

class RankSerializer(serializers.ModelSerializer):
    user_name = serializers.CharField(source='user_id.name', read_only=True)

    class Meta:
        model = Rank
        fields = ('score', 'user_name')
