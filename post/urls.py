from django.conf.urls import patterns, url, include
from django.contrib import admin

from post import views

admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^add$', views.PostCreateView.as_view(), name='add_post'),
    url(r'^edit/(?P<pk>\d+)/$', views.PostEditView.as_view(), name='edit_post'),
    url(r'^$', views.PostListView.as_view(), name='posts'),

    url(r'^add/comment/(?P<post_pk>\d+)/$', views.CommentCreateView.as_view(), name='add_comment'),
)