from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.

class HelloAPIview(APIView):
    """Test API Vew"""

    def get(self, request, format=None):
        """Returns a list of API View features."""

        an_apiview = [
        'uses HTTP methods as functions (get, post, patch, put, delete)',
        'it is similar to a traditional Django view',
        'gives you the most control over your logic',
        'is mapped manually to urls'
        ]

        return Response({'message': 'Hello!', 'an_apiview': an_apiview})
