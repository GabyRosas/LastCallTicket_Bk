from django.db import models
from django.contrib.auth.models import User


class Transport(models.Model):
    transport_name = models.CharField(max_length=255)
    transport_type = models.CharField(max_length=50)

    def __str__(self):
        return self.transport_name


class Ticket(models.Model):
    departure_place = models.CharField(max_length=255)
    arrival_place = models.CharField(max_length=255)
    departure_date = models.DateTimeField()
    return_date = models.DateTimeField(null=True, blank=True)
    register_date = models.DateTimeField(auto_now_add=True)
    original_price = models.DecimalField(max_digits=10, decimal_places=2)
    proposed_price = models.DecimalField(max_digits=10, decimal_places=2)
    note = models.TextField(blank=True)
    user = models.ForeignKey(User, related_name='tickets', on_delete=models.CASCADE)
    transport = models.ForeignKey(Transport, related_name='tickets', on_delete=models.CASCADE)

    def __str__(self):
        return '__all__'

