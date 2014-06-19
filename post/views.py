from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.list import ListView
from django.core.urlresolvers import reverse

from post.forms import PostForm, CommentForm
from post.models import Post, Comment


class PostCreateView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'post/form.html'

    @property
    def success_url(self):
        return reverse('posts')


class PostListView(ListView):
    model = Post
    template_name = 'post/list.html'


class PostEditView(UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'post/form.html'

    @property
    def success_url(self):
        return reverse('posts')


class CommentCreateView(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'post/form.html'

    @property
    def success_url(self):
        return reverse('posts')

    def get_form_kwargs(self):
        form_kwargs = super(CommentCreateView, self).get_form_kwargs()
        post = Post.objects.get(pk=self.kwargs['post_pk'])
        instance = Comment(post=post)
        form_kwargs['instance'] = instance
        return form_kwargs
