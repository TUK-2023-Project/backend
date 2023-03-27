# serializers.py 파일은 모델 인스턴스를 JSON 형식으로 변환하는 작업을 수행
from rest_framework import serializers
from .models import Rank

class RankSerializer(serializers.ModelSerializer):
    user_id = serializers.ReadOnlyField(source='user_id.id')

    class Meta:
        model = Rank
        fields = ('id', 'user_id', 'rank', 'score', 'created_at', 'updated_at', 'is_deleted')
        read_only_fields = ('id', 'rank', 'created_at', 'updated_at', 'is_deleted')