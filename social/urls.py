from django.urls import path
from .views import follow_user

urlpatterns = [
    path(
        'follow/<str:username>/',
        follow_user,
        name='follow_user'
    ),
]