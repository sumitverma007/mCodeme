from django.db import models

# Create your models here.
class memobj(models.Model):
    mem_id=models.AutoField(primary_key=True)
    mem_tag=models.CharField(max_length=50)
    mem_img=models.ImageField(upload_to="meme/images")

    def __str__(self):
        return self.mem_tag