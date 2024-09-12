from django.contrib import admin
from .models import Ticket, Transport

@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = ('departure_place', 'arrival_place', 'departure_date', 'return_date', 'original_price', 'proposed_price', 'user', 'transport')
    # Otros ajustes de administración aquí

@admin.register(Transport)
class TransportAdmin(admin.ModelAdmin):
    list_display = ('transport_name', 'transport_type')
    # Otros ajustes de administración aquí