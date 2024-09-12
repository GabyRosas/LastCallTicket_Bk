import pytest
from decimal import Decimal
from django.contrib.auth.models import User
from ticket_app.models import Ticket, Transport
from ticket_app.serializer import TicketSerializer
from django.utils import timezone


@pytest.mark.django_db
def test_ticket_serializer_create():

    user = User.objects.create_user(username='testuser', password='12345')
    transport = Transport.objects.create(transport_name='Bus Company', transport_type='Bus')

    data = {
        'departure_place': 'New York',
        'arrival_place': 'Los Angeles',
        'departure_date': timezone.make_aware(timezone.datetime(2024, 9, 12, 15, 30)),
        'return_date': None,
        'original_price': '250.00',
        'proposed_price': '200.00',
        'note': 'Cambio de nombre gratis',
        'user': user.id,
        'transport': transport.id
    }

    serializer = TicketSerializer(data=data)
    assert serializer.is_valid(), serializer.errors
    ticket = serializer.save()

    assert ticket.departure_place == 'New York'
    assert ticket.arrival_place == 'Los Angeles'
    assert ticket.original_price == Decimal('250.00')
    assert ticket.proposed_price == Decimal('200.00')
    assert ticket.note == 'Cambio de nombre gratis'
    assert ticket.user == user
    assert ticket.transport == transport