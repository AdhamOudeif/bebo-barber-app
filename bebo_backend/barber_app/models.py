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

class Review(models.Model):
    appointment = models.ForeignKey(
        'barber_app.Appointment',  # Ensure this matches your app name
        on_delete=models.CASCADE,
        related_name='reviews'
    )
    client = models.ForeignKey(
        'barber_app.User',
        on_delete=models.CASCADE,
        related_name='client_reviews',
        limit_choices_to={"role": "client"}  # Limit to clients
    )
    barber = models.ForeignKey(
        'barber_app.User',
        on_delete=models.CASCADE,
        related_name='barber_reviews',
        limit_choices_to={"role": "barber"}  # Linked to barbers
    )
    rating = models.PositiveIntegerField(help_text="Rating between 1 and 5", default=5)
    feedback = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'review'
        verbose_name = 'Review'
        verbose_name_plural = 'Reviews'

    def __str__(self):
        return f"Review by {self.client.name} for {self.barber.name}"
    

class Payment(models.Model):
    PAYMENT_METHOD_CHOICES = [
        ('card', 'Card'),
        ('wallet', 'Wallet'),
    ]
    PAYMENT_STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('successful', 'Successful'),
        ('failed', 'Failed'),
    ]

    appointment = models.OneToOneField(Appointment, on_delete=models.CASCADE)
    client = models.ForeignKey(User, on_delete=models.CASCADE, related_name='client_payments')
    barber = models.ForeignKey(User, on_delete=models.CASCADE, related_name='barber_payments')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method = models.CharField(max_length=10, choices=PAYMENT_METHOD_CHOICES)
    payment_status = models.CharField(max_length=10, choices=PAYMENT_STATUS_CHOICES, default='pending')
    transaction_id = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Payment {self.id} - {self.payment_status}"

    

