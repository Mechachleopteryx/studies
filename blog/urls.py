from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
    '',
    # url(r'^$', views.MainPage.as_view()),
    url(r'^post/', include('post.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
