from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, JsonResponse
from django.contrib.auth import authenticate, login
from .forms import LoginForm, UserRegistrationForm, UserEditForm, ProfileEditForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Profile, Contact
from django.contrib import messages
from django.views.decorators.http import require_POST
from common.decorators import ajax_required
from content.forms import TweetCreateForm
from content.models import Tweet
from actions.models import Action
from actions.utils import create_action


@login_required
def home(request):
    """home page displaying tweets from those you follow."""
    # Display all actions by default
    actions = Action.objects.filter(verb='tweeted')
    # user.following.values_list('id') # <QuerySet [(11,)]>
# user.following.values_list('id', flat=True) # <QuerySet [11]>
    following_ids = request.user.following.values_list('id', flat=True)

    if following_ids:
        # If user is following others, retrieve only their actions
        actions = actions.filter(user_id__in=following_ids)
    # actions = actions[:10]
    actions = actions.select_related('user', 'user__profile').prefetch_related('target')[:10]

    if request.method == 'POST':
        form = TweetCreateForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            tweet = Tweet.objects.create(user=request.user, body=cd['body'])
            tweet.save()

            form = TweetCreateForm()
            messages.success(request, 'Your tweet is published <a href="{% url "content:tweet_detail" %}">View</a>')

        else:
            messages.error(request, 'Error while processing your form.')
    else:
        form = TweetCreateForm()

    context = {'section': 'home','form': form, 'actions': actions}
    return render(request, 'users/index.html', context)

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(
                request, username=cd['username'], password=cd['password']
            )
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('Authenticated Successfully')
                else:
                    return HttpResponse('The link that you followed was broken')
            else:
                return HttpResponse('The credentials that you provided didn\'t match to an account.')
    else:
        form = LoginForm()

    context = {'form': form}
    # return render(request, '../content/templates/content/tweet/tweet_create.html', context)
    return render(request, 'users/login.html', context)


def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            # Set the chosen password
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            Profile.objects.create(user=new_user)
            create_action(new_user, 'has created an account')
            login(request, new_user)
            return render(request, 'users/home.html', {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request, 'users/register.html', {'user_form': user_form})


def user_list(request):
    users = User.objects.filter(is_active=True)
    return render(request, 'users/list.html', {'users': users})

def user_detail(request, username):
    user = get_object_or_404(User, username=username, is_active=True)
    return render(request, 'users/detail.html', {'section': 'profile', 'user': user})


@login_required
def edit(request):
    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user, data=request.POST)
        profile_form = ProfileEditForm(instance=request.user.profile, data=request.POST, files=request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Profile updated successfully')
        else:
            messages.error(request, 'Error updating your profile')
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile)
    return render(request, 'users/edit.html', {'section': 'more','user_form': user_form, 'profile_form': profile_form})


@ajax_required
@require_POST
@login_required
def user_follow(request):
    user_id = request.POST.get('id')
    action = request.POST.get('action')
    if user_id and action:
        try:
            user = User.objects.get(id=user_id)
            if action == 'follow':
                Contact.objects.get_or_create(
                    user_from=request.user,
                    user_to=user
                )
                create_action(request.user, 'is following', user)
            else:
                Contact.objects.filter(user_from=request.user, user_to=user).delete()
            return JsonResponse({'status':'ok'})
        except User.DoesNotExist:
            return JsonResponse({'status':'error'})
    return JsonResponse({'status':'error'})
