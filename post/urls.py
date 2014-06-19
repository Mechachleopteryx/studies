from django.conf.urls import patterns, url, include

from post.views import PostCreateView

urlpatterns = patterns(
    url(r'^add$', PostCreateView.as_view(), name='users'),
)