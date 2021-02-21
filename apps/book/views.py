from .models import Author, Book

from .serializers import AuthorSerializer, BookSerializer

from rest_framework import viewsets


class AuthorViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Author to be viewed or edited.
    """

    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class BookViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Book to be viewed or edited.
    """

    queryset = Book.objects.all()
    serializer_class = BookSerializer
