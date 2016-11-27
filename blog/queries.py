from galery.models import Photo_miniture, Photo


def photo_all_qr():
    return Photo.objects.all()
