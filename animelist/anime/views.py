from django.shortcuts import render, redirect
from django.http import Http404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib import messages
from .models import Anime
from .forms import RegisterForm

def home(request):
    anime = Anime.objects.all()
    return render(request, 'home.html', {
        'anime': anime,
    })

def anime_detail(request, anime_id):
    try:
        anime = Anime.objects.get(id=anime_id)
    except Anime.DoesNotExist:
        raise Http404('Anime not found')
    return render(request, 'anime_detail.html', {
        'anime': anime,
    })



def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log the user in after successful registration
            return redirect('home')
    else:
        form = RegisterForm()
    return render(request, 'registration/register.html', {'form': form})
