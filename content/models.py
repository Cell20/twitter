from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.auth.models import User
from .fields import OrderField
from django.utils import timezone
import math
from django.contrib.humanize.templatetags import humanize
import calendar
from django.conf import settings

# Module            Tweet 1 (main tweet of the thread)
#   Content 1           Tweet 2
#   Content 2           Tweet 3

# reach my state by python manage.py runserver go to http://127.0.0.1:8000/admin/content/tweet/
# add image plus other options on Tweet model set required no or blank false

class Tweet(models.Model):
    """realted name allows as user.tweets"""
    user = models.ForeignKey(User, related_name="tweets", on_delete=models.DO_NOTHING)
    body = models.CharField(max_length=200)
    image = models.ImageField(upload_to=f'data/tweet_media/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    users_like = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='tweets_liked', blank=True)
    

    def __str__(self):
        now = timezone.now()
        
        diff= now - self.created_at

        if diff.days == 0 and diff.seconds >= 0 and diff.seconds < 60:
            seconds= diff.seconds
            
            if seconds == 1:
                return f"@{self.user.username} {str(seconds)}second\n{self.body}\n{self.image}"
            
            else:
                return f"@{self.user.username} {str(seconds)} seconds ago\n{self.body}\n{self.image}"

            

        if diff.days == 0 and diff.seconds >= 60 and diff.seconds < 3600:
            minutes= math.floor(diff.seconds/60)

            if minutes == 1:
                return f"@{self.user.username} {str(minutes)} minute ago\n{self.body}\n{self.image}"
            
            else:
                return f"@{self.user.username} {str(minutes)} minutes ago\n{self.body}\n{self.image}"



        if diff.days == 0 and diff.seconds >= 3600 and diff.seconds < 86400:
            hours= math.floor(diff.seconds/3600)

            if hours == 1:
                return f"@{self.user.username} {str(hours)} hour ago\n{self.body}\n{self.image}"

            else:
                return f"@{self.user.username} {str(hours)} hours ago\n{self.body}\n{self.image}"

        # 1 day to 30 days
        if diff.days >= 1 and diff.days < 30:
            days= diff.days
        
            if days == 1:
                return f"@{self.user.username} {str(days)} day ago\n{self.body}\n{self.image}"

            else:
                return f"@{self.user.username} {str(days)} days ago\n{self.body}\n{self.image}"

        if diff.days >= 30 and diff.days < 365:
            months= math.floor(diff.days/30)
            

            if months == 1:
                return f"@{self.user.username} {str(months)} month ago\n{self.body}\n{self.image}"

            else:
                return f"@{self.user.username} {str(months)} months ago\n{self.body}\n{self.image}"


        if diff.days >= 365:
            years= math.floor(diff.days/365)

            if years == 1:
                return f"@{self.user.username} {str(years)} year ago\n{self.body}\n{self.image}"

            else:
                return f"@{self.user.username} {str(years)} years ago\n{self.body}\n{self.image}"


    def whenpublished(self):
        now = timezone.now()

        n = self.created_at.date().month
        
        tweet_day = self.created_at.date().day
        tweet_month = calendar.month_name[n][:3]
        tweet_year = self.created_at.date().year 

        diff = now - self.created_at

        if diff.days == 0 and diff.seconds >= 0 and diff.seconds < 60:
            seconds= diff.seconds
            return f"{str(seconds)}s"            

        if diff.days == 0 and diff.seconds >= 60 and diff.seconds < 3600:
            minutes= math.floor(diff.seconds/60)
            return str(minutes) + "m"


        if diff.days == 0 and diff.seconds >= 3600 and diff.seconds < 86400:
            hours= math.floor(diff.seconds/3600)
            return str(hours) + "h"

        # 1 day to 30 days
        if diff.days >= 1 and diff.days < 365:
            return f"{tweet_day} {tweet_month}"

        if diff.days >= 365:
            return f"{tweet_day} {tweet_month} {tweet_year}"






'''
class Content(models.Model):
    content_type = models.ForeignKey(ContentType, on_delete=models.DO_NOTHING, limit_choices_to={'model__in':('tweet', 'image', 'video')})
    object_id = models.PositiveIntegerField()
    item = GenericForeignKey('content_type', 'object_id')

class ItemBase(models.Model):
    owner = models.ForeignKey(User, related_name='%(class)s_related', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True
        ordering = ['-created']

class Tweet(ItemBase):
    tweet = models.TextField(max_length=50)

class Image(ItemBase):
    file = models.FileField(upload_to='images')

class Video(ItemBase):
    url = models.URLField()


class Tweet(models.Model):
    owner = models.ForeignKey(User, related_name='%(class)s_related', on_delete=models.CASCADE)
    tweet = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.tweet

class ChildTweet(models.Model):
    owner = models.ForeignKey(User, related_name='%(class)s_related', on_delete=models.DO_NOTHING)
    tweet = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)
'''
