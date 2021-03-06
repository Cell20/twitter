from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views
from content import views as cv
from django.urls import reverse_lazy

app_name = 'users'

urlpatterns = [
    path('', views.home, name='home'),
    path('followers/', views.user_list, name='user_list'),
    path('users/follow/', views.user_follow, name='user_follow'),
    # post views
    # path('login/', views.user_login, name='login'),

    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    # path('', include('django.contrib.auth.urls')),

    # change password urls
    path('password_change/', auth_views.PasswordChangeView.as_view(success_url=reverse_lazy('users:password_change_done')), name='password_change'),
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),

    # reset password urls
    path('password_reset/', auth_views.PasswordResetView.as_view(success_url=reverse_lazy('users:password_reset_done')), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(success_url=reverse_lazy('users:password_reset_complete')), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),

    path('register/', views.register, name='register'),

    # user home page when he can see all his tweets
    # there should be a link to edit profile too on template.
    path('users/', views.user_list, name='user_list'),
    path('<username>/', views.user_detail, name='user_detail'),
    # profile edit
    path('edit/', views.edit, name='edit'),

]
