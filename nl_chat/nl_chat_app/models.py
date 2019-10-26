from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted([(item, item) for item in get_all_styles()])


class Message(models.Model):
    received_time = models.DateTimeField(auto_now_add=True)
    sender = models.TextField()
    content = models.TextField()
    reply_sent = models.BooleanField(default=False)


    class Meta:
        ordering = ['received_time']


