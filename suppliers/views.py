from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

# Create your views here.
from suppliers.models import Suppliers
from suppliers.serializers import SuppliersSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters

class SuppliersView(viewsets.ModelViewSet):
    queryset = Suppliers.objects.all()
    serializer_class = SuppliersSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
    ]
    search_fields = ["city"]