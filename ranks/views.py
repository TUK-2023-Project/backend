from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Rank
from .serializers import RankSerializer
from django.contrib.auth import get_user_model
from users.models import UserData
from itertools import groupby
from rest_framework.exceptions import AuthenticationFailed
from utils import get_user_id_from_token
from django.db.models import IntegerField

User = get_user_model()

class RankView(APIView):
  
      
    """
    이름 : 정태원
    내용 : score정보를 DB에 저장합니다.
    날짜 : 3/30
    """

    def post(self, request):
        token = request.META.get('HTTP_ACCESS', None)
       
        if token is None:
         return Response({'message': '토큰이 필요합니다'}, status=status.HTTP_404_NOT_FOUND)

        try:
            user_id = get_user_id_from_token(token.split(' ')[1])
        except AuthenticationFailed as e:
            return Response({'message': str(e)}, status=status.HTTP_401_UNAUTHORIZED)
        
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

        return Response(status=status.HTTP_201_CREATED)


    """
    이름 : 정태원
    내용 : 상위 10개의 랭킹정보와 사용자 id값을 배열로 return합니다. 동점자의 경우 같은 순위를 처리합니다.
    날짜 : 3/30
    """
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

class UserRankView(APIView):
    """
    이름 : 정태원
    내용 : 토큰으로부터 입력받은 특정 사용자의 랭킹정보를 return해주는 코드입니다
    날짜 : 4/10
    """
    def get(self, request):
        token = request.META.get('HTTP_ACCESS', None)
        if token is None:
            return Response({'message': '토큰이 필요합니다'}, status=status.HTTP_404_NOT_FOUND)

        try:
            user_id = get_user_id_from_token(token.split(' ')[1])
        except AuthenticationFailed as e:
            return Response({'message': str(e)}, status=status.HTTP_401_UNAUTHORIZED)

        user_rank = Rank.objects.filter(user_id=user_id).first()
        if not user_rank:
            return Response({'message': '해당 유저의 랭킹 정보가 없습니다.'}, status=status.HTTP_404_NOT_FOUND)

        ranks = Rank.objects.filter(score__gte=user_rank.score)
        rank = ranks.count()

        return Response({'rank': rank}, status=status.HTTP_200_OK)
