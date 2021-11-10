from .models import Post
from celery import Celery, shared_task
from celery.schedules import crontab


app = Celery()

app.conf.beat_schedule = {
    'reset_upvotes-every-30-seconds': {
        'task': 'tasks.upvotes',
        'schedule': 30.0
    },
}
app.conf.timezone = 'UTC'


@shared_task
def reset_upvotes():
    posts = Post.objects.all()
    for post in posts:
        post.upvotes.clear()



