from django.db import models

# Create your models here.

class Moviedata(models.Model):
    def __str__(self) -> str:
        return self.name

    name = models.CharField(max_length=200)
    duration = models.FloatField()
    rating = models.FloatField()
    catagory = models.CharField(max_length=200, default='action')
    image = models.ImageField(upload_to='Image', default='Image/NoImage/noimage.jpg')

