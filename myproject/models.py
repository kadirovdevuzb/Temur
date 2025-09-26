from django.db import models

class Yangiliklar(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/', )

class Filmlar(models.Model):
    title = models.CharField(max_length=50)
    genre = models.CharField(max_length=30)
    year = models.IntegerField(default=0)
    rating = models.FloatField(default=0)
    
    def __str__ (self):
        return self.title