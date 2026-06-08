from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    description = models.TextField()
    image = models.ImageField(upload_to='products/')
    weight = models.CharField(max_length=50, default='500g')

    def __str__(self):
        return self.name