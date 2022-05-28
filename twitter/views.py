from django.shortcuts import get_object_or_404, render
from .models import Profile
from django.contrib.auth.models import User

    
def dashboard(request):
    return render(request, "base.html")

def user_list(request):
    users = User.objects.exclude(username=request.user.username)
    return render(request, "twitter/user_list.html", {"users": users})

def user_detail(request, username):
    user = get_object_or_404(User, username=username)  #is_active=T for blocking ;)
    return render(request, "twitter/user_detail.html", {"user": user})

# Profile() got an unexpected argument username
