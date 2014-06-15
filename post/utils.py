import json
import urllib
import datetime
from random import choice

from post.models import Post, Comment


def import_news(category_id, category_tags=()):
    data = urllib.urlopen(
        'http://api.feedzilla.com/v1/categories/{}/'
        'articles.json'.format(category_id)).read()
    data_json = json.loads(data)
    for news in data_json['articles']:
        post = Post.objects.create(
            title=news['title'],
            content=news['summary'],
            tags=', '.format(category_tags),
            created=datetime.datetime.strptime(news['publish_date'][:-6],
                                               '%a, %d %b %Y %H:%M:%S'),
            views=choice(range(0, 1000))
        )

        while True:
            if not choice([True, False]):
                break
            Comment.objects.create(
                post=post,
                full_name='Mr {}'.format(choice(range(0, 1000))),
                value='Lorem ipsum...'
            )
            print('created comment for {}'.format(post.id))

    print('imported: {}'.format(len(data_json['articles'])))


def create_extra():
    data = [
        {
            'title': 'Google',
            'content': 'Google maps..',
            'tags': ', '.format(['maps', 'hotfix', 'google']),
            'created': datetime.datetime(2014, 5, 11, 20, 16, 43, 512387),
            'views': 2,
        },
        {
            'title': 'Google',
            'content': 'Google drive..',
            'tags': ', '.format(['drive', 'google']),
            'created': datetime.datetime(2014, 5, 11, 20, 16, 43, 512387),
            'views': 3,
        },
        {
            'title': 'I love Google!',
            'content': 'Google',
            'tags': ', '.format(['love', 'google']),
            'created': datetime.datetime(2014, 5, 11, 20, 16, 43, 512387),
            'views': 4,
        },

    ]

    for kwargs in data:
        Post.objects.get_or_create(**kwargs)


def import_all():
    import_news(15, category_tags=['IT'])
    import_news(30, category_tags=['Technology'])
    create_extra()
