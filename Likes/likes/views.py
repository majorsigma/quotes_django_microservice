from django.shortcuts import render
import requests
from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .producer import publish


from likes.models import Quote, QuoteUser
from likes.serializers import QuoteSerializer, QuoteUserSerializer


class QuoteViewSet(viewsets.ModelViewSet):
    queryset = Quote.objects.all()
    serializer_class = QuoteSerializer


class QuoteUserViewSet(viewsets.ModelViewSet):
    queryset = QuoteUser.objects.all()
    serializer_class = QuoteUserSerializer


@api_view(['GET'])
def like(request, pk, format=None):
    query = {'username': 'john'}
    req = requests.get('http://localhost:8000/users/', params=query)
    data = req.json()
    print("Data from Quotes: %s" % data)

    try:
        print("Id from data: %s" % data[0]['id'])
        if data[0]['id']:
            quoteuser = QuoteUser.objects.create(
                user_id=data[0]['id'], quote_id=pk)
            quoteuser.save()
            publish('quote_liked', pk)
            print('Quoteuser created')
            return Response('Quote liked...', status=status.HTTP_201_CREATED)

    except Exception as e:
        return Response({"error": "You can only like a qoute once"}, status=status.HTTP_400_BAD_REQUEST)
