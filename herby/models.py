from django.db import models
from django.utils import timezone

# Create your models here.

# 선생님의 클래스 이름 = Post
class Post(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    myuni = models.TextField()
    body = models.TextField()

    def __str__(self):
        return self.title
    
    def summary(self):
        return self.body[:40]

class Comment(models.Model):
    post = models.ForeignKey('herby.Post', related_name='comments', on_delete=models.CASCADE)
    author_name = models.CharField(max_length = 200)
    text = models.TextField()
    created_Date = models.DateTimeField(default = timezone.now)

    def __str__(self):
        return self.text