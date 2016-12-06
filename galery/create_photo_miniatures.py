import os
from sys import platform
from PIL import Image
from galery.models import Photo, Photo_miniture


if platform == "win32":
    MEDIA_FILES_PATH = r'C:\Users\oplawsze\media_files'
if platform == 'linux':
    MEDIA_FILES_PATH = r'/home/Oskar/LuizaLos/'


SIZE = 128, 128


def fill_db():
    """
    refactor me pls
    Returns:

    """
    Photo_miniture.objects.all().delete()
    for photo in Photo.objects.all():
        save_path = MEDIA_FILES_PATH
        img = Image.open(photo.image)
        img.thumbnail(SIZE, Image.ANTIALIAS)
        name_of_file = photo.title + 'mini.jpg'
        completeName = os.path.join(save_path, name_of_file)
        img.save(completeName, "JPEG")
        # print(platform)
        # print(os.path.abspath(photo.image))
        # print(os.path.abspath(completeName))
        # print(os.path.basename(completeName))
        # print(os.path.realpath(completeName))
        # print(os.path.relpath(completeName))
        Photo_miniture.objects.get_or_create(
            big_photo=photo,
            title=photo.title,
            desctiption=photo.desctiption,
            # image=os.path.basename('/media/' + name_of_file),
            image=os.path.basename(name_of_file),
            timestamp=photo.timestamp
        )