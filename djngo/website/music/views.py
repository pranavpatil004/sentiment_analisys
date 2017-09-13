from django.http import HttpResponse
from music.models import Album, Song
from django.shortcuts import render, get_object_or_404


def index(request):
    all_albums = Album.objects.all()
    context = {
        'all_albums': all_albums,
    }
    return render(request, "music/index.html", context)


def detail(request, album_id):
    album = get_object_or_404(Album, pk=album_id)
    return render(request,"music/detail.html", {'album':album})


def song_detail(request, song_title):
    return HttpResponse("<h2>Details for song: " + song_title + "</h2>")

def favourite(request, album_id):
    album = get_object_or_404(Album, pk=album_id)
    try:
        selected_song = album.song_set.get(pk=request.POST['song'])
    except (KeyError, Song.DoesNotExist):
        return render(request,"music/detail.html", {
            'album':album,
            'error_message':'You did not select valid song',
        })
    else:
        selected_song.is_favourite = True
        selected_song.save()
        return render(request, "music/detail.html", {'album': album})
