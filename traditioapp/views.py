from django.shortcuts import render
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from .forms import *


@login_required(login_url='login')
def index(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
    else:
        form = PostForm()

    try:
        trad = Traditonsongs.objects.all()
        profiles = Profile.objects.all()
        song = Songs.objects.all()
        late = LatestContact.objects.all()
        posts = Post.objects.all()

        index_data = {
            'trad': trad,
            'profiles': profiles,
            'songses': song,
            'late': late,
            'posts': posts,
            'form': form,
        }

    except Traditonsongs.DoesNotExist:
        posts = None
        trad = None
        profiles = None
        song = None
        late = None
    return render(request, 'main/index.html', index_data)


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('index')
    else:
        form = SignupForm()
    return render(request, 'registration/signup.html', {'form': form})


@login_required(login_url='login')
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.trad = request.user.profile.county
            post.owner = request.user
            post.save()
    else:
        form = PostForm()
    return render(request, 'model_temp/add_posts.html', {'form': form})


@login_required(login_url='login')
def create_trad(request):
    if request.method == 'POST':
        form =TraditionForm(request.POST, request.FILES)
        if form.is_valid():
            trad = form.save(commit=False)
            trad.save()
    else:
        form =TraditionForm
    return render(request, 'model_temp/add_trads.html', {'form': form})


@login_required(login_url='login')
def create_songs(request):
    if request.method == 'POST':
        form = SongsForm(request.POST, request.FILES)
        if form.is_valid():
            print(form)
            song = form.save(commit=False)
            song.save()
    else:
        form = SongsForm
    return render(request, 'model_temp/add_song.html', {'form': form})


@login_required(login_url='login')
def create_latest(request):
    if request.method == 'POST':
        form = LatestForm(request.POST, request.FILES)
        if form.is_valid():
            latest = form.save(commit=False)
            latest.save()
    else:
        form = LatestForm
    return render(request, 'model_temp/add_latest.html', {'form': form})


def about(request):
    name = 'rita'
    return render(request, 'main/about.html', {'name': name})


def profile(request, username):
    return render(request, 'main/profile.html')


def edit_profile(request, username):
    user = User.objects.get(username=username)
    if request.method == 'POST':
        form = UpdateProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            form.save()
            return redirect('profile', user.username)
    else:
        form = UpdateProfileForm(instance=request.user.profile)
    return render(request, 'editing/edit_profile.html', {'form': form})


def search_results(request):
    if 'search' in request.GET and request.GET['search']:
        search_term = request.GET.get('search')
        print(search_term)
        searched_photos = Traditonsongs.search_by_title(search_term)
        print(searched_photos)
        message = f'{search_term}'
        params = {
            'searched_photos': searched_photos,
            'message': message,
        }

        return render(request, 'search_results.html', params)

    else:
        message = 'Ooppss, You did not search for anything.'
        return render(request, 'main/search_results.html', locals())
