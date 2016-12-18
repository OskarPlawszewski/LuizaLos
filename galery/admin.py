from django.contrib import admin
from galery.models import Photo
from galery.models import Photo_miniture
from galery.signals import delete_photo_miniature, create_photo_miniature


class PhotoAdmin(admin.ModelAdmin):
    list_display = ["title", "timestamp"]

    class Meta:
        model = Photo

admin.site.register(Photo, PhotoAdmin)


class PhotoMiniAdmin(admin.ModelAdmin):
    list_display = ["title", "timestamp"]

    class Meta:
        model = Photo_miniture

admin.site.register(Photo_miniture, PhotoMiniAdmin)

# Register your models here.
