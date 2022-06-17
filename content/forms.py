from django import forms
from .models import Tweet


class TweetCreateForm(forms.ModelForm):
    class Meta:
        model = Tweet
        fields = ('body', 'image') # gotta add GIF, poll, emoji, schedule, location
        labels = {
            'body': (''),
            'image': (''),
        }
        help_texts = {
            'image': (''),
        }

        widgets = {
            'body': forms.Textarea(attrs={'placeholder': 'What\'s happening', 'cols': 40, 'rows': 1}),
        }
        error_messages = {
            'body': {
                'max_length': ("This tweet is too long."),
            },
        }

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['body'].widget.attrs.update({'placeholder': 'What\'s happening?'})                  
