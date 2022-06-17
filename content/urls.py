from django.urls import path, include
from . import views
from django.urls import reverse_lazy

app_name = 'content'

urlpatterns = [
    # How to pass views.tweet_create to users:home ?
    # path('tweet_create/', views.tweet_create, name='tweet_create'),
    path('<username>/status/<int:id>/', views.tweet_detail, name='tweet_detail'),
    path('like/', views.tweet_like, name='like'),
]
