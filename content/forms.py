from django import forms
from .models import Tweet

class TweetCreateForm(forms.ModelForm):
    class Meta:
        model = Tweet
        fields = ('body', 'image') # gotta add GIF, poll, emoji, schedule, location


        widget= forms.TextInput (attrs={'placeholder':"What's happening?"})
                    # 'class':'tweetform',
                    # 'id':'tweetform',
                    
