from django.db import models

# Create your models here.

from users.models import *
from signlanguage.models import *

# User = get_user_model()

class Incorrect(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(UserData, on_delete=models.CASCADE, related_name='incorrect', db_column='user_id')
    sign_id = models.ForeignKey(SignWord, on_delete=models.CASCADE, related_name='incorrect', db_column='sign_id')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)

    class Meta:
        db_table = 'incorrect'