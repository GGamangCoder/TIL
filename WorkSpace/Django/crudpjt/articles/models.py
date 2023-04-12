from django.db import models

# Create your models here.
# 모델 작성 = 테이블 스키마 정의
class Article(models.Model):
    title = models.CharField(max_length=16)
    content = models.TextField()
    image = models.ImageField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)