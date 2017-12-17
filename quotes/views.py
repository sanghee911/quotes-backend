from .models import Quote
from .serializers import QuoteSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class QuoteList(APIView):
    """
    List all quote, or create a new snippet.
    """
    def get(self, request, format=None):
        todo = Quote.objects.all()
        serializer = QuoteSerializer(todo, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = QuoteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)