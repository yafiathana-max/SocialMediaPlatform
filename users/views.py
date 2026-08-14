from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import RegisterForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()

            login(request, user)

            return redirect('home')
    else:
        form = RegisterForm()

    return render(request, 'register.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')

        return render(request, 'login.html', {
            'error': 'Invalid username or password.'
        })

    return render(request, 'login.html')


def user_logout(request):
    logout(request)
    return redirect('login')

def home(request):
    from posts.models import Post

    posts = Post.objects.all().order_by('-created_at')

    return render(request, 'home.html', {
        'posts': posts
    })

def profile(request, username):
    from social.models import Follow

    profile_user = User.objects.get(username=username)

    followers_count = Follow.objects.filter(
        following=profile_user
    ).count()

    following_count = Follow.objects.filter(
        follower=profile_user
    ).count()

    is_following = False

    if request.user.is_authenticated:
        is_following = Follow.objects.filter(
            follower=request.user,
            following=profile_user
        ).exists()

    return render(request, 'profile.html', {
        'profile_user': profile_user,
        'is_following': is_following,
        'followers_count': followers_count,
        'following_count': following_count,
    })

@login_required
def edit_profile(request):
    from .models import Profile

    profile, created = Profile.objects.get_or_create(
        user=request.user
    )

    if request.method == 'POST':
        profile.bio = request.POST.get('bio', '')
        profile.save()

        return redirect(
            'profile',
            username=request.user.username
        )

    return render(request, 'edit_profile.html', {
        'profile': profile
    })