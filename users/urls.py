from django.urls import path
from .views import register, user_login, user_logout, home, profile, edit_profile

urlpatterns = [
    path('', home, name='home'),
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('profile/<str:username>/', profile, name='profile'),
    path('edit-profile/', edit_profile, name='edit_profile'),
]