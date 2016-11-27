from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from galery.fill_miniatures_in_db import fill_db
from galery.models import Photo


@receiver(post_save, sender=Photo)
def handle_pronto_for_user_statistics(instance, **kwargs):
    fill_db()
