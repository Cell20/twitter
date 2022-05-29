from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse, resolve


class SignupTests(TestCase):
    username = 'newuser'
