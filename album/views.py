from django.shortcuts import render

from .models import Album
# Create your views here.
def album(request):

    album = Album.objects.all()

    context = {
        'albums': album
    }

    return render(request, 'album/index.html', context)


def blueberry(request):


    context = {
        
    }

    return render(request, 'album/blueberry.html', context)