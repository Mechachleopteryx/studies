from django import forms

from post.models import Post, Comment


class PostForm(forms.ModelForm):
    class Meta:
        model = Post


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ('post', )