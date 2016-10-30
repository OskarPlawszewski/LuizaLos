from django.shortcuts import render
from galery.models import Photo

def photo_list(request):
    queryset = Photo.objects.all()
    context = {
        'photos': queryset,
    }

    return render(request, 'blog/photo.html', context)

def photo_latest(request):
    queryset = Photo.objects.latest('timestamp')
    context = {
        'photo': queryset,
    }

    return render(request, 'blog/main_page.html', context)
# Create your views here.
