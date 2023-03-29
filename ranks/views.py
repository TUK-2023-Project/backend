from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Rank
from .serializers import RankSerializer
from django.contrib.auth import get_user_model
from users.models import UserData
from itertools import groupby
from rest_framework_jwt.utils import jwt_decode_handler

User = get_user_model()

def get_user_id_from_token(token):
    decoded_token = jwt_decode_handler(token)
    user_id = decoded_token['user_id']
    return user_id

class RankView(APIView):
  
    
    def post(self, request):
        token = request.META.get('HTTP_AUTHORIZATION', '').split(' ')[1]
        user_id = get_user_id_from_token(token)
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
        ranks = Rank.objects.all().order_by('-score')
        rank_list = list(ranks)

        groups = []
        for k, g in groupby(rank_list, key=lambda x: x.score):
            groups.append(list(g))

        response_data = []
        rank = 1
        for group in groups:
            for r in group:
                serializer = RankSerializer(r)
                data = serializer.data
                user = UserData.objects.get(pk=r.user_id.id)
                data['user_name'] = user.name
                data['rank'] = rank
        
                response_data.append(data)
            rank += len(group)

        return Response(response_data[:10], status=status.HTTP_200_OK)
