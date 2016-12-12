from django.shortcuts import render
from galery.models import Photo, Photo_miniture
from django.shortcuts import get_object_or_404
import PIL


def photo_detail(request, pk):
    queryset = get_object_or_404(Photo, pk=pk)
    context = {
        'photo': queryset,
    }
    return render(request, 'blog/photo_detail.html', context)


def photo_list(request):
    queryset = Photo_miniture.objects.all()
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
