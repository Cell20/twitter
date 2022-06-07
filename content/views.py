from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import TweetCreateForm


@login_required
def tweet_create(request):
    if request.method == 'POST':
        tweet_form = TweetCreateForm(request.POST)
        if tweet_form.is_valid():
            new_tweet = tweet_form.save(commit=False)
            new_tweet.user = request.user
            new_tweet.save()
            messages.success(request, 'Your tweet is published <a href="{% url "content:tweet_detail" %}">View</a>')
            return render(request, 'user/detail.html', {'new_tweet': new_tweet})
    else:
        tweet_form = TweetCreateForm()   

    return render(request, 'content/tweet/tweet_create.html', {'tweet_form': tweet_form})
