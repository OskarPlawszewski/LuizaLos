from django.db.models.signals import post_save
from django.dispatch import receiver
from galery.fill_db import fill_db
from galery.models import Photo


@receiver(post_save, sender=Photo)
def handle_pronto_for_user_statistics():
    fill_db()
