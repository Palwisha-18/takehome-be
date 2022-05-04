from api.models import Home
from api.serializers import HomeSerializer
from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveUpdateDestroyAPIView


class HomeCreateView(CreateAPIView):
    queryset = Home.objects.all()
    serializer_class = HomeSerializer


class HomeListView(ListAPIView):
    queryset = Home.objects.all()
    serializer_class = HomeSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['home_type', 'state', 'zipcode', 'num_bathrooms', 'num_bedrooms']


class HomeRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = Home.objects.all()
    serializer_class = HomeSerializer
    lookup_field = "uuid"
