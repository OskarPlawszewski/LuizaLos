from django.db import models
from django.db.models.fields.files import ImageField
from PIL import Image
# from PIL import ImageField

class Photo(models.Model):
    title = models.CharField(max_length=100)
    width = models.IntegerField(default=0)
    height = models.IntegerField(default=0)
    image = models.ImageField(null=False, blank=False, width_field='width', height_field='height')
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    # updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ["-timestamp"]
