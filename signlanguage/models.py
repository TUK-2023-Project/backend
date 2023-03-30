import uuid
from django.db import models
class SignWord(models.Model):
    sign_id = models.IntegerField(primary_key=True)
    #id=models.IntegerField()(primary_key=True, Autoin, editable=False, null=False)
    word = models.CharField(max_length=100, unique=True)
    #user_id=models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, null=False)
    wordtype = models.CharField(max_length=100)
    context = models.CharField(max_length=100)
    photo_url = models.CharField(max_length=100,default=False)
    created_at = models.DateTimeField(auto_now_add=True, null=False)
    updated_at = models.DateTimeField(auto_now=True, null=False)
    is_deleted=models.BooleanField(default=False)




    class Meta:
        db_table = 'signword'


