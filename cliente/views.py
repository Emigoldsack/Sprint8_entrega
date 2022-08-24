from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Cliente
from .serializer import ClienteSerializer

# Create your views here.

class CustomerDetails(APIView):
    def get(self,request, pk):
        customer = Cliente.objects.filter(pk=pk).first()
        serializer = ClienteSerializer(customer)

        if customer:
            return Response(serializer.data, status = status.HTTP_200_OK)
        return Response(serializer.error_messages, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk):
        updateCustomer = Cliente.objects.filter(pk=pk).first()
        serializer = ClienteSerializer(updateCustomer, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CustomerList(APIView):

    def post(self, request, format=None):
        serializer = ClienteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        customers = Cliente.objects.all()
        serializer = ClienteSerializer(customers, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)



