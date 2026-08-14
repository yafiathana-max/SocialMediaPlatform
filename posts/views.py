from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Post


@login_required
def create_post(request):
    if request.method == 'POST':
        content = request.POST.get('content')

        if content:
            Post.objects.create(
                author=request.user,
                content=content
            )

            return redirect('home')

    return render(request, 'create_post.html')

@login_required
def add_comment(request, post_id):
    if request.method == 'POST':
        content = request.POST.get('content')

        if content:
            from .models import Comment

            Comment.objects.create(
                post_id=post_id,
                author=request.user,
                content=content
            )

    return redirect('home')

@login_required
def like_post(request, post_id):
    from .models import Like

    post = Post.objects.get(id=post_id)

    like, created = Like.objects.get_or_create(
        post=post,
        user=request.user
    )

    if not created:
        like.delete()

    return redirect('home')

from django.shortcuts import get_object_or_404


def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    return render(request, 'post_detail.html', {
        'post': post
    })