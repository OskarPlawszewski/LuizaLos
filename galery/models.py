from django.db import models
from django.db.models.fields.files import ImageField
from PIL import Image
import inspect, os


class Photo(models.Model):
    title = models.CharField(max_length=100)
    desctiption = models.CharField(max_length=100)
    width = models.IntegerField(default=0)
    height = models.IntegerField(default=0)
    image = models.ImageField(null=False, blank=False, width_field='width', height_field='height')
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ["-timestamp"]


class Photo_miniture(models.Model):
    # big_photo = models.ForeignKey(Photo, null=True)
    title = models.CharField(max_length=100)
    desctiption = models.CharField(max_length=100)
    width = models.IntegerField(default=0)
    height = models.IntegerField(default=0)
    image = models.ImageField(null=False, blank=False, width_field='width', height_field='height')
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ["-timestamp"]


def shrink_photo(photo):
    maxsize = (100, 100)
    return photo.thumbnail(maxsize, Image.ANTIALIAS)


SIZE = 128, 128


def fill_db():
    """
    refactor me pls
    Returns:

    """
    Photo_miniture.objects.all().delete()
    for photo in Photo.objects.all():
        save_path = r'C:\Users\oplawsze\media_files'
        img = Image.open(photo.image)
        img.thumbnail(SIZE, Image.ANTIALIAS)
        name_of_file = photo.title + 'mini.jpg'
        completeName = os.path.join(save_path, name_of_file)
        img.save(completeName, "JPEG")
        Photo_miniture.objects.get_or_create(
            title=photo.title,
            image=os.path.abspath(completeName),
        )
