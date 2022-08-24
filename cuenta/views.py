from ssl import ALERT_DESCRIPTION_UNKNOWN_PSK_IDENTITY
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from Sprint_8.HomeBanking.cliente.models import Cliente
from .models import Cuenta
from .serializer import CuentaSerializer
from cliente.models import Cliente

# Create your views here.

class AccountBalance(APIView):
    def get(self, request, pk):
        customer_id = Cliente.customer_id
        account = Cuenta.objects.filter(pk = customer_id ).first
        serializer = CuentaSerializer(account)
    
        if account:
            return Response(serializer.data, status = status.HTTP_200_OK)
        return Response(serializer.error_messages, status=status.HTTP_404_NOT_FOUND)
