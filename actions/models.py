from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey


class Action(models.Model):
    user = models.ForeignKey('auth.User', related_name='actions', db_index=True, on_delete=models.CASCADE)
    verb = models.CharField(max_length=255)
    target_ct = models.ForeignKey(ContentType, blank=True, null=True, related_name='target_obj', on_delete=models.CASCADE) # , limit_choices_to={'id__gte': 13}
    target_id = models.PositiveIntegerField(null=True, blank=True, db_index=True)
    target = GenericForeignKey('target_ct', 'target_id')
    created = models.DateTimeField(auto_now_add=True, db_index=True)

    def __str__(self):
        return f'{self.user.username} {self.verb} {self.target}'

    class Meta:
        ordering = ('-created',)

# cost of 1 gram of gold = 4405.0
# cost of 1 gram of gold = 4605.0
# 
