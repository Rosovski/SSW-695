from django.db import models
from django.urls import reverse
from store.models import Store


class Product(models.Model):
    title = models.CharField(max_length=120)
    image = models.ImageField(blank=True, null=True)
    description = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=20)
    category = models.TextField(blank=True, null=True)
    featured = models.BooleanField(default=False)
    store = models.ForeignKey(Store, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse("product-detail", kwargs={"id": self.id})
