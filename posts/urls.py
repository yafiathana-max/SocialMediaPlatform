from django.urls import path
from .views import create_post, add_comment, like_post, post_detail


urlpatterns = [
    path('create/', create_post, name='create_post'),
    path(
        '<int:post_id>/comment/',
        add_comment,
        name='add_comment'
    ),
    path(
        '<int:post_id>/like/',
        like_post,
        name='like_post'
    ),
    path(
    '<int:post_id>/',
    post_detail,
    name='post_detail'
),
]