from django.db import models
from sorl.thumbnail import ImageField

# Create your models here.
class Image(models.Model):
    title = models.CharField(max_length=100)
    image = ImageField(upload_to='images/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
