from django.db import models
from django.contrib.auth.models import User

# Create your models here.      

class UserStickers(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE)    
    id_complete = models.CharField(max_length=6)
    country = models.CharField(max_length=3, null=True)    
    created = models.DateTimeField(auto_now_add = True)
    has = models.BooleanField(default=False)
    repeated = models.BooleanField(default=False)
    count = models.IntegerField(default=0)
    
    def __str__(self):
        return str(self.id_complete)
    
