from django.test import TestCase
from django.db.models import signals
from django.dispatch import receiver
from galery.models import Photo, Photo_miniture
import galery.signals


@receiver(signals.pre_save, sender=Photo)
def handle_pronto_for_user_statistics(sender, **kwargs):
    print('dupa')



class TestSignals(TestCase):

    def test_photo_miniature_automatization(self):
        photo = Photo()
        photo.title = 'some title'
        photo.save()
        self.assertEqual(len(Photo.objects.all()), len(Photo_miniture.objects.all()))
