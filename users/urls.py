from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views
from django.urls import reverse_lazy

app_name = 'users'

urlpatterns = [
    # post views
    # path('login/', views.user_login, name='login'),

    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('', views.home, name='home'),
    # path('', include('django.contrib.auth.urls')),

    # change password urls
    path('password_change/', auth_views.PasswordChangeView.as_view(success_url=reverse_lazy('users:password_change_done')), name='password_change'),
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),
]
