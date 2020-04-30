from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.


class Product(models.Model):
    title = models.CharField(max_length=120)
    image = models.ImageField(blank=True, null=True)
    description = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=20)
    category = models.TextField(blank=True, null=True)
    featured = models.BooleanField(default=False)
    store = models.TextField(default="Unknown Store")

    def get_absolute_url(self):
        return reverse("product-detail", kwargs={"id": self.id})


class Comment(models.Model):
    product = models.ForeignKey('products.Product', related_name='comments', on_delete=models.CASCADE)
    author = models.CharField(max_length=120)
    rating = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(100)])
    content = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.product.title
    
    def get_absolute_url(self):
        return reverse("product-list")