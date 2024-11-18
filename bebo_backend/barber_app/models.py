from django.db import models

class User(models.Model):
    ROLE_CHOICES = [
        ('barber', 'Barber'),
        ('client', 'Client'),
    ]

    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=20, unique=True)
    password = models.CharField(max_length=255)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)
    profile_image = models.URLField(blank=True, null=True)
    location_lat = models.DecimalField(max_digits=10, decimal_places=8, blank=True, null=True)
    location_long = models.DecimalField(max_digits=11, decimal_places=8, blank=True, null=True)
    is_verified = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        app_label = 'backend'
        db_table = 'users'

    def __str__(self):
        return self.name

