from django.db import models

# Create your models here.
class ItemTypeIndex(models.Model):
    id = models.CharField(max_length=100, primary_key=True)
    name = models.CharField(max_length=100)
    path = models.CharField(max_length=200)

    def __str__(self):
        return self.id