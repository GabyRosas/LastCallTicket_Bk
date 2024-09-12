from django.shortcuts import render
from rest_framework import viewsets
from .serializer import TicketSerializer, TransportSerializer
from .models import Ticket, Transport


class TicketView(viewsets.ModelViewSet):
    serializer_class = TicketSerializer
    queryset = Ticket.objects.all()


class TransportView(viewsets.ModelViewSet):
    serializer_class = TransportSerializer
    queryset = Transport.objects.all()

