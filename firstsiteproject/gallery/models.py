from django.db import models

# Create your models here.
class Gallery(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')
    place = models.CharField(max_length=100)

    def __str__(self):
        return self.title