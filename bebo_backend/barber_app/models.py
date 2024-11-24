from datetime import datetime
from django.db import models
from django.contrib.auth import get_user_model

# User = get_user_model()

class User(models.Model):
    ROLE_CHOICES = [
        ('barber', 'Barber'),
        ('client', 'Client'),
    ]

    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=20)
    password = models.CharField(max_length=255)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)
    profile_image = models.URLField(blank=True, null=True)
    location_lat = models.DecimalField(max_digits=10, decimal_places=8, blank=True, null=True)
    location_long = models.DecimalField(max_digits=11, decimal_places=8, blank=True, null=True)
    is_verified = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        app_label = 'barber_app'
        db_table = 'users'

    def __str__(self):
        return self.name
    
class Service(models.Model):
    barber = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="services",
        limit_choices_to={"role": "barber"},  # Ensures only barbers can have services
    )
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    duration = models.IntegerField(help_text="Duration in minutes")
    price = models.DecimalField(max_digits=10, decimal_places=2)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} - {self.barber.name}"
    class Meta:
        db_table = 'services'

class Appointment(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
    ]

    PAYMENT_STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('completed', 'Completed'),
        ('failed', 'Failed'),
    ]

    client = models.ForeignKey(
        User, 
        on_delete=models.CASCADE, 
        related_name='appointments_as_client'
    )
    barber = models.ForeignKey(
        User, 
        on_delete=models.CASCADE, 
        related_name='appointments_as_barber'
    )
    service = models.ForeignKey(
        Service, 
        on_delete=models.CASCADE
    )
    scheduled_at = models.DateTimeField()
    status = models.CharField(
        max_length=10, 
        choices=STATUS_CHOICES, 
        default='pending'
    )
    notes = models.TextField(null=True, blank=True)
    payment_status = models.CharField(
        max_length=10, 
        choices=PAYMENT_STATUS_CHOICES, 
        default='pending'
    )
    created_at = models.DateTimeField(default=datetime.now()) # may need to update field
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Appointment {self.id} - {self.client.name} with {self.barber.name}"
    
    class Meta:
        db_table = 'appointments'
    

