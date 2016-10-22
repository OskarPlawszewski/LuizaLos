from django.db import models
from django.db.models.fields.files import ImageField
from PIL import Image

class Photo(models.Model):
    caption = models.CharField(max_length=64, blank=True)
    blob = ImageField(
        upload_to='BlobStorage',
        max_length=255,
        blank=False,
    )
    # serving_url = models.URLField()