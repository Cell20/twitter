from django.db import models
from django.conf import settings

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_of_birth = models.DateField(blank=True, null=True)
    photo = models.ImageField(upload_to=f'{user.username}/data/profile_media/', blank=True)

    def __str__(self):
        return f'Profile for user {self.user.username}'
