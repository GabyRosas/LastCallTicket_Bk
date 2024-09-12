import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from django.contrib.auth.models import User
from ticket_app.models import Ticket, Transport

@pytest.mark.django_db
def test_ticket_list():
    client = APIClient()

    user = User.objects.create_user(username='testuser', password='12345')
    transport = Transport.objects.create(transport_name='Bus Company', transport_type='Bus')

    Ticket.objects.create(
        departure_place='New York',
        arrival_place='Los Angeles',
        departure_date='2024-09-12T15:30:00Z',
        return_date=None,
        original_price='250.00',
        proposed_price='200.00',
        note='First class seat',
        user=user,
        transport=transport
    )

    url = reverse('ticket-list')
    response = client.get(url)

    assert response.status_code == status.HTTP_200_OK
    assert len(response.data) > 0
    assert response.data[0]['departure_place'] == 'New York'

@pytest.mark.django_db
def test_ticket_create():

    client = APIClient()

    user = User.objects.create_user(username='testuser', password='12345')
    transport = Transport.objects.create(transport_name='Bus Company', transport_type='Bus')

    data = {
        'departure_place': 'Boston',
        'arrival_place': 'Chicago',
        'departure_date': '2024-10-01T09:00:00Z',
        'return_date': '2024-10-05T18:00:00Z',
        'original_price': '300.00',
        'proposed_price': '250.00',
        'note': 'Cambio de nombre gratis',
        'transport': transport.id,
        'user': user.id
    }

    url = reverse('ticket-list')
    response = client.post(url, data, format='json')

    assert response.status_code == status.HTTP_201_CREATED

    assert response.data['departure_place'] == 'Boston'
    assert response.data['arrival_place'] == 'Chicago'
    assert response.data['original_price'] == '300.00'
