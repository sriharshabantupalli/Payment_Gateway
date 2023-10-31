from django.urls import path
from .views import *

urlpatterns = [
    path('payment/', PaymentAPIView.as_view(), name='payment-api'),
]