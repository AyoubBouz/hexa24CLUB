from django.db import models

# Create your models here.
class Project(models.Model):
    chef =models.CharField(max_length=50)
    pname =models.CharField(max_length=50)
    nature=models.CharField(max_length=50)

    def __str__(self):
        return self.pname
