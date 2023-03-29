from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Rank
from .serializers import RankSerializer
from django.contrib.auth import get_user_model
from users.models import UserData
from itertools import groupby


User = get_user_model()

class RankView(APIView):
    def post(self, request):
        user_id = request.data.get('user_id')
        score = request.data.get('score')

        if not user_id or not score:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        user = User.objects.filter(id=user_id).first()
        if not user:
            return Response({'message': '존재하지 않는 유저 입니다'}, status=status.HTTP_404_NOT_FOUND)

        rank = Rank.objects.filter(user_id=user.id).first()
        if not rank:
            rank = Rank(user_id=user, score=0)

        if score > rank.score or rank.score is None:
            rank.score = score
            rank.save()

        serializer = RankSerializer(rank)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def get(self, request):
        ranks = Rank.objects.all().order_by('rank')[:10]
        serializer = RankSerializer(ranks, many=True)
        response_data = []
        for data in serializer.data:
            user = UserData.objects.get(pk=data['user_id'])
            data['user_name'] = user.name
            del data['user_id']
            response_data.append(data)
        return Response(response_data, status=status.HTTP_200_OK)
