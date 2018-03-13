from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

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

