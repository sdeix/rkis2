from django.shortcuts import render
from rest_framework import generics, viewsets
from rest_framework import filters
# from django_filters.rest_framework import DjangoFilterBackend

from .permissions import IsAdminOrReadOnly
from .serializers import BookSerializer, AuthorSerializer
from .models import Book, Author
# Create your views here.

class BookAPIView(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = (IsAdminOrReadOnly,)
    filter_backends = [filters.SearchFilter]
    search_fields= ["title","author__name","genre"]
      

class AuthorAPIView(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer  
    permission_classes = (IsAdminOrReadOnly,)

