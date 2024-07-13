from django.db import models

# Create your models here.

class Movie(models.Model):
    id = models.IntegerField(null=False, primary_key=True)
    name = models.CharField(max_length=40, null=False)
    genre = models.CharField(max_length=25, null=False)
    director = models.CharField(max_length=40, null=False)
    year = models.IntegerField(null=False)
    sinopsis = models.TextField(null=False)
    
    def __str__(self) -> str:
        return self.name
    
    
