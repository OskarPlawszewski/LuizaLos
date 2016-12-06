from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from galery.create_photo_miniatures import fill_db
from galery.models import Photo


@receiver(post_save, sender=Photo)
def handle_pronto_for_user_statistics(instance, **kwargs):
    fill_db()
