from django.db import models

class Anime(models.Model):
    name = models.CharField(max_length=200)
    producer = models.CharField(max_length=200)
    release_date = models.DateField()
    image = models.ImageField(upload_to='anime_images/', blank=True, null=True)
    description = models.TextField()

    def __str__(self):
        return self.name




