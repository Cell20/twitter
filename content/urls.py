from django.urls import path
from . import views
from django.urls import reverse_lazy

app_name = 'content'

urlpatterns = [
    # path('status/<pk>/', views.tweet_detail, name='tweet_detail'),
    path('tweet_create/', views.tweet_create)
]
