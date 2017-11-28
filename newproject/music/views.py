from django.http import Http404
from .models import Album
from django.shortcuts import render
def index(request):

    all_albums= Album.objects.all()

    return render(request,'music/index.html',{'all_albums':all_albums})



def detail(request,album_id):

    try:
      album= Album.objects.get(pk=album_id)

    except Album.DoesNotExists:
        raise Http404("Album does not exists")
    return render(request,'music/detail.html',{'album':album})
