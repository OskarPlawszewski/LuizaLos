from django.contrib import admin
from galery.models import Photo


class PhotoAdmin(admin.ModelAdmin):
    list_display = ["title", "timestamp"]

    class Meta:
        model = Photo

admin.site.register(Photo, PhotoAdmin)

# Register your models here.
