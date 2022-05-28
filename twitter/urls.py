from django.urls import path
from .views import dashboard, user_list, user_detail

app_name = "twitter"

urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('explore/', user_list, name='user_list'),
    path('<username>/', user_detail, name='user_detail'),
]
