from django.shortcuts import render, redirect
from .models import *

def index(request):
    return render(request, "index.html")

def dashboard(request):
    return redirect('/')

def single_album(request, album_id):
    return redirect('/')

def create(request):
    # Adding this logic to succesfully create an album in the view function
    if request.method == 'POST':
        Album.objects.create(title = request.POST['title'], artist = request.POST['artist'], year = request.POST['year'])
    return redirect('/')

def edit(request, album_id):
    Album.objects.filter(id=1).update(title = request.POST['title'], artist = request.POST['artist'], year = request.POST['year'])
    return redirect('/')

def delete(request, album_id):
    Album.objects.get(id=1).delete()[0]

def read(request, album_id):
    Album.objects.get(id=1)
    context = {
        id : album_id
    }
    return render(request, "index.html", context)