from django.shortcuts import render
from rest_framework import viewsets, mixins

# Create your views here.
from .serializers import ClientSerializer
from apps.crm.models import Client


class ClientList(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer