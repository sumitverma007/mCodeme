from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User

# Create your models here.
class memobj(models.Model):
    mem_id=models.AutoField(primary_key=True)
    mem_tag=models.CharField(max_length=50)
    mem_img=models.ImageField(upload_to="meme/images")

    def __str__(self):
        return self.mem_tag

class memeComment(models.Model):
    sno=models.AutoField(primary_key=True)
    comment=models.TextField()
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    memepost=models.ForeignKey(memobj,on_delete=models.CASCADE)
    parent=models.ForeignKey('self',on_delete=models.CASCADE,null=True)
    timestamp=models.DateTimeField(default=now)

    def __str__(self):
        return "comment by"+self.user.username        