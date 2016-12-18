from django.db.models import signals
from django.dispatch import receiver
from galery.models import Photo
from galery.fill_db import fill_db


@receiver(signals.post_save, sender=Photo)
def create_photo_miniature(sender, **kwargs):
    fill_db()


@receiver(signals.post_delete, sender=Photo)
def delete_photo_miniature(sender, **kwargs):
    fill_db()
