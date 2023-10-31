from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import PaymentOrder, PaymentLog
from .serializers import PaymentOrderSerializer, PaymentLogSerializer
from django.core.cache import cache


class PaymentAPIView(APIView):
    def post(self, request):
        try:
            # Check if the payment data is cached
            cache_key = f'payment_{request.data["card"]["number"]}'  # Create a unique cache key
            cached_data = cache.get(cache_key)

            if cached_data:
                # Use the cached data
                return Response(cached_data, status=status.HTTP_201_CREATED)

            serializer = PaymentOrderSerializer(data=request.data)
            if serializer.is_valid():
                payment_order = serializer.save()

                # Log the payment
                PaymentLog.objects.create(order=payment_order, status="success", authorization_code="SDSD23232333")

                # Cache the payment data for future requests
                cache.set(cache_key, serializer.data, timeout=3600)  # Cache for 1 hour

                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            # Handle exceptions, log the error, and return an appropriate error response
            error_message = str(e)
            # Log the error using your preferred logging mechanism
            return Response({"error": error_message}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)