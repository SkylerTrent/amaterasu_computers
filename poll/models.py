
# Create your models here.
from django.db import models
"""
Sets up 2 models:
The Poll model to register votes for each voteable product.
The voted model to keep a list of emailadresses of users
that have voted.
"""


class Poll(models.Model,):
    product_type = models.CharField(max_length=254, default='')
    votes = models.IntegerField(default=0)
    image_url = models.URLField(max_length=1024, null=True, blank=True)

    def __str__(self):
        return self.product_type


class Voted(models.Model,):
    user_email = models.CharField(max_length=128, default='')

    def __str__(self):
        return self.user_email
