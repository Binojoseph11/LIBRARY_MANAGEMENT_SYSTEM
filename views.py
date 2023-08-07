from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework.generics import CreateAPIView
from rest_framework.generics import DestroyAPIView
from rest_framework.generics import UpdateAPIView
from book.serializers import bookserializer
from book.models import book
from rest_framework import generics
from rest_framework import filters

# Create your views here.
class ListbookAPIView(ListAPIView):
    """This endpoint list all of the available book from the database"""
    queryset = book.objects.all()
    serializer_class = bookserializer

class CreatebookAPIView(CreateAPIView):
    """This endpoint allows for creation of a book"""
    queryset = book.objects.all()
    serializer_class = bookserializer

class UpdatebookAPIView(UpdateAPIView):
    """This endpoint allows for updating a specific book by passing in the id of the book to update"""
    queryset = book.objects.all()
    serializer_class = bookserializer

class DeletebookAPIView(DestroyAPIView):
    """This endpoint allows for deletion of a specific book from the database"""
    queryset = book.objects.all()
    serializer_class = bookserializer




class QuestionsAPIView(generics.ListCreateAPIView):
    filter_backends = (filters.SearchFilter,)
    search_fields = ['Author_name','Book_name','book_assigned_to']
    
    queryset = book.objects.all()
    serializer_class = bookserializer