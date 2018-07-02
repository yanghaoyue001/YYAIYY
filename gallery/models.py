from django.db import models
from django.utils import timezone

# Create your models here.
class Photoshow(models.Model):
    title = models.TextField()
    photo = models.ImageField('photos/noimage.jpg')
    created_date = models.CharField(max_length=8)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
