from django.db import models

# Create your models here.

class content(models.Model):
    username =  models.CharField(max_length=200)
    email =  models.EmailField()
    body = models.TextField()
    def __str__(self):
        return self.username