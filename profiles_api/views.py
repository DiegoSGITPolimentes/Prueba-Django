from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from . import serializers
from rest_framework import status
from rest_framework import viewsets
# Create your views here.

class HelloApiView(APIView):
    """Test API view."""
    def get(self, request, format=None):
        """Return a list of API features"""
        an_apiview = [
            'Uses HTTTP methods as function (get, post, put, patch, delete)',
            'It is similar to a tradictional DJango view',
            'Gives you the most control over your logic',
            'Is mapped manually to URLs'
        ]
        return Response({'message': 'Hello world', 'an_apiview': an_apiview})
    def post(self, request):
        serializer = serializers.HelloSerializer(data=request.data)
        if serializer.is_valid():
            name = serializer.data.get('name')
            message = 'Hello {0}'.format(name)
            return Response({'message': message})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        """ Handles updating an object. """
        return Response({'method': 'put'})

    def patch(self, request, pk=None):
        """ Patch request, only updates fields provided in the request. """
        return Response({'method': 'patch'})

    def delete(self, request, pk=None):
        """ Deletes an object. """
        return Response({'method': 'delete'})

class HelloViewSet(viewsets.ViewSet):
    """ Tests API ViewSet. """
    def lsit(self, request):
        """ Return a Hello message. """

        a_viewset = [
            'Uses actions (list, create, retrieve, update, partial_update, destroy)',
            'Automatically maps to URLs using Routers',
            'Provides more functionality with less code.'
        ]

        return Response({'message': 'Hello', 'a_viewset': a_viewset})
