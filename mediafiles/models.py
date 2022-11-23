from django.db import models

# Create your models here.

class Media(models.Model):
    image = models.ImageField(upload_to = 'photos/cover',blank = True, null = True)
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name