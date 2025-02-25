from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class PostModel(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created_at', '-updated_at')

    def comment_count(self):
        return self.comment_set.all().count()
    
    def comments(self):
        return self.comment_set.all()


    def __str__(self):
        return self.title
    
class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(PostModel, on_delete=models.CASCADE)
    content = models.TextField(max_length=1000)

    def __str__(self):
        return self.content


