from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.shortcuts import get_object_or_404
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib import messages
from .forms import TweetCreateForm
from .models import Tweet
from django.http import HttpResponse
from actions.utils import create_action


@login_required
def tweet_create(request):
    if request.method == 'POST':
        form = TweetCreateForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            tweet = Tweet.objects.create(user=request.user, body=cd['body'])
            # messages.success(request, 'Your tweet is published <a href="{% url "content:tweet_detail" %}">View</a>')
            tweet.save()
            create_action(request.user, 'tweeted', tweet)
            return HttpResponse('Tweeted Successfully')
        else:
            return HttpResponse("Data isn't valid")
    else:
        form = TweetCreateForm()

    context = {'form': form}
    return render(request, 'content/tweet/tweet_create.html', context)


def tweet_detail(request, username, id):
    tweet = get_object_or_404(Tweet, id=id)
    return render(request, 'content/tweet/tweet_detail.html', {'section': 'home','tweet': tweet})


@login_required
@require_POST
def tweet_like(request):
    tweet_id = request.POST.get('id')
    action = request.POST.get('action')
    if tweet_id and action:
        try:
            tweet = Tweet.objects.get(id=tweet_id)
            if action == 'like':
                tweet.users_like.add(request.user)
                create_action(request.user, 'liked', tweet)
            else:
                tweet.users_like.remove(request.user)
            return JsonResponse({'status':'ok'})
        except:
            pass
    return JsonResponse({'status':'error'})
