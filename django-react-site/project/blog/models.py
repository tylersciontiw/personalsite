from django.db import models

class BlogPost(models.Model):
    title = models.CharField(max_length=100)
    tag = models.CharField(max_length = 50)
    post_body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
