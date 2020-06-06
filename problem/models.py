from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now
from django.contrib.auth import authenticate,login,logout
# Create your models here.
class probobj(models.Model):
    p_id=models.AutoField(primary_key=True)
    p_user=models.ForeignKey(User,on_delete=models.CASCADE)
    p_tag=models.CharField(max_length=100,default="unnamed")
    p_name=models.CharField(max_length=100)
    p_desc=models.TextField()
    p_in=models.CharField(max_length=200,default="")
    p_out=models.CharField(max_length=200,default="")
    p_const=models.CharField(max_length=200,default="")
    p_exin=models.CharField(max_length=200,default="")
    p_exout=models.CharField(max_length=200,default="")
    p_code=models.TextField(default="")
    p_timestamp=models.DateTimeField(default=now)

    def __str__(self):
        return "added by "+self.p_user.username+" on "+self.p_tag


