"""
Sets up 2 models:
The Giveaway Model which keeps track of user product votes.
The Has_Voted Model keeps track of user email
addresses that have previously voted.
"""

from django.db import models


class Giveaway(models.Model,):
    give_away_item = models.CharField(max_length=254, default='')
    votes = models.IntegerField(default=0)
    image_url = models.URLField(max_length=1024, blank=True)

    def __str__(self):
        return self.give_away_item


class Has_Voted(models.Model,):
    user_email = models.CharField(max_length=128, default='')

    def __str__(self):
        return self.user_email
