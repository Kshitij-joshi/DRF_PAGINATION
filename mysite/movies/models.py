from django.db import models

# Create your models here.
class Moviedata(models.Model):
    name = models.CharField(max_length=200)
    duration = models.FloatField()
    rating = models.FloatField()
    category = models.CharField(max_length=200,default="family")
    image = models.ImageField(upload_to="Images/",default = "images/None/Noimg.jpg")

    class Meta:
        verbose_name = "Movie Data"
        verbose_name_plural = "Movie Data"

    def __str__(self):
        return self.name

class Movies(models.Model):
    name = models.CharField(max_length=200)
    average_rating = models.FloatField()

    class Meta:
        verbose_name = "Movie"
        verbose_name_plural = "Movies"

    def __str__(self):
        return self.name