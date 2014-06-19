from django.shortcuts import render
from django.views.generic.edit import CreateView

from post.forms import PostForm
from post.models import Post


class PostCreateView(CreateView):
    model = Post
    form_class = PostForm
    success_url = '/success'