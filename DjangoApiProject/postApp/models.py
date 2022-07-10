#postApp/models.py 코드
from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=50) #제목
    content = models.TextField() #내용
    updated_at = models.DateTimeField(auto_now=True) #작성 일자