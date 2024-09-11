from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Ticket, Transport

class TransportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transport
        fields = '__all__'


class TicketSerializer(serializers.ModelSerializer):
    transport = serializers.PrimaryKeyRelatedField(queryset=Transport.objects.all())
    username = serializers.CharField(source='user.username', read_only=True)
    class Meta:
        model = Ticket
        fields = '__all__'

    def get_username(self, obj):
        return obj.user.username


    def update(self, instance, validated_data):
        # Actualiza los campos del Ticket
        instance.departure_place = validated_data.get('departure_place', instance.departure_place)
        instance.arrival_place = validated_data.get('arrival_place', instance.arrival_place)
        instance.departure_date = validated_data.get('departure_date', instance.departure_date)
        instance.return_date = validated_data.get('return_date', instance.return_date)
        instance.original_price = validated_data.get('original_price', instance.original_price)
        instance.proposed_price = validated_data.get('proposed_price', instance.proposed_price)
        instance.note = validated_data.get('note', instance.note)

        validated_data.pop('user', None)

        # Actualiza el campo transport si está presente en los datos validados
        if 'transport' in validated_data:
            instance.transport_id = validated_data.get('transport')

        instance.save()
        return instance

