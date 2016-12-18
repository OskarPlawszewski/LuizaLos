from django.db.models import signals
from django.dispatch import receiver
from galery.models import Photo
from galery.fill_db import fill_db


@receiver(signals.post_save, sender=Photo)
def handle_pronto_for_user_statistics(sender, **kwargs):
    fill_db()
