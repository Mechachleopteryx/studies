from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=64)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    tags = models.CharField(max_length=200, null=True, blank=True)


class Comment(models.Model):
    post = models.ForeignKey('post.Post')
    full_name = models.CharField(max_length=64)
    value = models.TextField()