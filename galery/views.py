from django.shortcuts import render
from galery.models import Photo
import PIL


def shrink_photo(photo):
    maxsize = (100, 100)
    return photo.thumbnail(maxsize, PIL.Image.ANTIALIAS)


def photo_list(request):
    queryset = Photo.objects.all()
    for i in queryset:
        print(Photo.objects.all().values())
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
