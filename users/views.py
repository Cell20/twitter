from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from .forms import LoginForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


@login_required
def home(request):
    """home page displaying tweets from those you follow."""
    return render(request, 'users/home.html', {'section': 'home'})


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data

            if User.objects.filter(username=cd['username']).exists():
                if User.objects.get(username=cd['username']).check_password('localpasswd'):
                    user = authenticate(request, username=cd['username'], password=cd['password'])
                    if user is not None:
                        if user.is_active:
                            login(request, user)
                            return HttpResponse('Authenticated successfully')                        
                        else:
                            return HttpResponse('The link that you followed was broken')
                    else:
                        return HttpResponse('The credentials that you provided didn\'t match to an account.')
                else:
                    return HttpResponse(f"Incorrect Password")
            else:
                return HttpResponse(f"The username @{cd['username']} doesn't exist.")
    else:
        form = LoginForm()
    return render(request, 'users/login.html', {'form': form})
