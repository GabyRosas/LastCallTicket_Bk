from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TicketView, TransportView

router = DefaultRouter()
router.register(r'tickets', TicketView)
router.register(r'transports', TransportView)

urlpatterns = [
    path('', include(router.urls)),
]