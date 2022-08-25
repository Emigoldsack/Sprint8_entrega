from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Cuenta
from .serializer import CuentaSerializer
from cliente.models import Cliente

# Create your views here.

class AccountBalance(APIView):
    def get(self, request):
        account = Cuenta.objects.all()
        serializer = CuentaSerializer(account, many = True)
        return Response(serializer.data, status = status.HTTP_200_OK)
      
