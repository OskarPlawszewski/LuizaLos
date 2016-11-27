from django.contrib import admin
from galery.models import Photo
from galery.models import Photo_miniture


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
