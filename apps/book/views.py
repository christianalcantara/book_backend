from .models import Author, Book
from ..rent.models import Rent
from ..rent.serializers import RentSerializer
from .serializers import AuthorSerializer, BookSerializer

from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action

from rest_framework import authentication, permissions


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

    @action(
        methods=["post"],
        detail=True,
        authentication_classes=[authentication.TokenAuthentication],
        permission_classes=[],
        url_path="rent",
        url_name="rent-book",
        name="Rent",
    )
    def rent(self, request, pk=None):
        """
        Returns a list of all the group names that the given
        user belongs to.
        """
        book = self.get_object()
        user = request.user
        if user.is_authenticated:
            if book.is_available:
                rent = Rent.objects.create(
                    user=user,
                    book=book
                )
                rent_serializer = RentSerializer(rent, context={'request': request})
                return Response(status=status.HTTP_200_OK, data=rent_serializer.data)
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST, data={"detail": f"Book: \'{book}\' is not available for rent."})
        return Response(status=status.HTTP_401_UNAUTHORIZED)
