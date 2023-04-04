import jwt
from rest_framework.exceptions import AuthenticationFailed
from django.conf import settings


"""
이름 : 정태원
함수 : get_user_id_from_token
내용 : 헤더로 넘어온 토큰정보를 복호화하여 userId를 반환하거나 예외를 발생시킵니다
날짜 : 3/30
"""

def get_user_id_from_token(token):
    try:
        decoded_token = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])
    except jwt.exceptions.ExpiredSignatureError:
        raise AuthenticationFailed('토큰이 만료되었습니다')
    except jwt.exceptions.DecodeError:
        raise AuthenticationFailed('토큰이 유효하지 않습니다')
    user_id = decoded_token['user_id']
    
    user = User.objects.filter(id=user_id, is_deleted=False).first()
    if not user:
        return Response({'message': '존재하지 않는 유저 입니다'}, status=status.HTTP_404_NOT_FOUND)
        
    return user_id