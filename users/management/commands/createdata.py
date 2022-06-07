from msilib.schema import Media
from django.core.management.base import BaseCommand
from faker import Faker
import faker.providers
from users.models import Profile
from django.contrib.auth.models import User
import urllib.request
from datetime import date
import os
import random
from content.models import Tweet
from decouple import config


# class Provider(faker.providers.BaseProvider):
    # """Class to provide custom which doesn't exist in faker to suit your needs"""


class Command(BaseCommand):
    help = "Command Information"

    def handle(self, *args, **kwargs):
        fake = Faker()
        # fake.add_provider(Provider)

        superusers = User.objects.filter(is_superuser=True)
        if len(superusers) < 1:
            superuser = User.objects.create_superuser(
                username='cell',
                email=config("EMAIL"),
                password=config("PASSWORD"),
            )

        for _ in range(5):
            user = fake.unique.first_name()
            user = User.objects.create(
                username=user, password=config("PASSWORD"), first_name=user, last_name=fake.last_name(), email=user+'@gmail.com')
            
            Profile.objects.create(user=user, date_of_birth=fake.date(), photo='/media/avatar.png')

            # Create tweets
            Tweet.objects.create(user=user, body=fake.sentence())
            users = User.objects.all()




        # Liking the Tweet
        # add_like = random.sample(
        #     list(users), random.randint(1, users.count()))
        # for im in Image.objects.all():
        #     for like in add_like:
        #         im.users_like.add(User.objects.get(id=like.id))

        # Though the above commands can create a Image cuz most fields
        # aren't required but u need to give everyfield value properly to cuz
        # you're in py shell which wasn't the case in UI

        # Follow each other
        # for _ in users:
            # Contact.objects.create(user_from=User.objects.get(id=random.randint(
                # 1, users.count())), user_to=User.objects.get(id=random.randint(1, users.count())))
