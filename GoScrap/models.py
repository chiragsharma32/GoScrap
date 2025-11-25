from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class PickupRequest(models.Model):
    """Model to store pickup requests from users"""
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='pickup_requests', null=True, blank=True)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    pickup_date = models.DateField()
    pickup_time = models.TimeField()
    pickup_address = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=[
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
    ], default='pending')
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return f"Pickup Request from {self.name} on {self.pickup_date}"
