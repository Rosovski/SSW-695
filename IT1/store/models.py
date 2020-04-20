from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from django.urls import reverse


class Store(models.Model):
    STORE_TYPES = (
        ('Restaurant', 'Restaurant'),
    )

    STATES = (
        ('SS', 'Select State'),
        ('AL', 'Alabama'), ('AK', 'Alaska'), ('AZ', 'Arizona'), ('AR', 'Arkansas'), ('CA', 'California'),
        ('CO', 'Colorado'), ('CT', 'Connecticut'), ('DE', 'Delaware'), ('FL', 'Florida'), ('GA', 'Georgia'),
        ('Hi', 'Hawaii'), ('ID', 'Idaho'), ('IL', 'Illinois'), ('IN', 'Indiana'), ('IA', 'Iowa'),
        ('KS', 'Kansas'), ('KY', 'Kentucky'), ('LA', 'Louisiana'), ('ME', 'Maine'), ('MD', 'Maryland'),
        ('MA', 'Massachusetts'), ('MI', 'Michigan'), ('MN', 'Minnesota'), ('MS', 'Mississippi'), ('MO', 'Missouri'),
        ('MT', 'Montana'), ('NE', 'Nebraska'), ('NV', 'Nevada'), ('NH', 'New Hampshire'), ('NJ', 'New Jersey'),
        ('NM', 'New Mexico'), ('NY', 'New York'), ('NC', 'North Carolina'), ('ND', 'North Dakota'), ('OH', 'Ohio'),
        ('OK', 'Oklahoma'), ('OR', 'Oregon'), ('PA', 'Pennsylvania'), ('RI', 'Rhode Island'), ('SC', 'South Carolina'),
        ('SD', 'South Dakota'), ('TN', 'Tennessee'), ('TX', 'Texas'), ('UT', 'Utah'), ('VT', 'Vermont'),
        ('VA', 'Virginia'), ('WA', 'Washington'), ('WV', 'West Virginia'), ('WI', 'Wisconsin'), ('WY', 'Wyoming'),
    )
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    store_name = models.CharField(max_length=250)
    description = models.CharField(max_length=1000, null=True)
    store_address = models.CharField(max_length=250)
    store_address_2 = models.CharField(max_length=250)
    mobile = models.PositiveIntegerField()
    email = models.EmailField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(
        max_length=100, choices=STATES, default='SS')
    country = models.CharField(max_length=20, default='United States')
    store = models.CharField(
        max_length=100, choices=STORE_TYPES, default='Restaurant')
    registration_date = models.DateField(default=timezone.now)

    def __repr__(self):
        return self.store_name

    # un-comment if you want to navigate to Store detail page after creating a new store.
    def get_absolute_url(self):
        return reverse('store-detail', kwargs={'pk': self.pk})