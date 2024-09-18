from django.db import models

class Product(models.Model):
    title = models.CharField(max_length=100)
    specs = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image_link = models.URLField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.title
