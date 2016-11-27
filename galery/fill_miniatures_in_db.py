from PIL import Image
from galery.models import Photo, Photo_miniture
import os


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