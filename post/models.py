from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=64)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    views = models.IntegerField()
    modified = models.DateTimeField(auto_now=True)
    tags = models.CharField(
        verbose_name=u'Related tags', max_length=200, null=True, blank=True)

    class Meta:
        ordering = ['-modified']

    def __unicode__(self):  # __str__ on Python 3
        return u'{}...'.format(self.title[:10])


class Comment(models.Model):
    post = models.ForeignKey('post.Post')
    full_name = models.CharField(max_length=64)
    value = models.TextField(help_text=u'Please be nice')

    def __unicode__(self):  # __str__ on Python 3
        return u'{} by {}'.format(self.value[:10], self.full_name)
