import pytest
from django.contrib.auth.models import User
from ticket_app.models import Ticket, Transport
from django.utils import timezone
from decimal import Decimal


@pytest.mark.django_db
def test_ticket_creation():

    user = User.objects.create_user(username='testuser', password='12345')

    transport = Transport.objects.create(transport_name='Bus Company', transport_type='Bus')

    ticket = Ticket.objects.create(
        departure_place='New York',
        arrival_place='Los Angeles',
        departure_date=timezone.make_aware(timezone.datetime(2024, 9, 16, 15, 30)),  # Fecha con zona horaria
        return_date=None,
        original_price=Decimal('250.00'),
        proposed_price=Decimal('180.00'),
        note='Cambio de nombre 15€',
        user=user,
        transport=transport
    )

    assert Ticket.objects.count() == 1
    assert ticket.departure_place == 'New York'
    assert ticket.arrival_place == 'Los Angeles'
    assert ticket.original_price == Decimal('250.00')
    assert ticket.proposed_price == Decimal('180.00')
    assert ticket.note == 'Cambio de nombre 15€'
    assert ticket.user == user
    assert ticket.transport == transport
