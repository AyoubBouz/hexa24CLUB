from django.db import models

# Create your models here.
class Event(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateField()
    text = models.TextField()
    slug = models.SlugField()
    affiche= models.ImageField(blank=True)

    def __str__(self):
        return self.title
