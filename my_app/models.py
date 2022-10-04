from django.db import models

# Create your models here.

class ImageModel(models.Model):
    title = models.CharField(max_length=30)
    desc = models.TextField()
    image = models.ImageField(upload_to='images/')
    date_added = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self) -> str:
        return f'{self.title}'