from rest_framework import serializers
from .models import Ticket, Transport

class TransportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transport
        fields = '__all__'


class TicketSerializer(serializers.ModelSerializer):
    transport = TransportSerializer()
    class Meta:
        model = Ticket
        fields = '__all__'

