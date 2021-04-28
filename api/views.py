from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import generics
from . models import Room, Category
from . serializers import RoomSerializer, CategorySerializer
from rest_framework.permissions import SAFE_METHODS, IsAuthenticated, IsAuthenticatedOrReadOnly, BasePermission, IsAdminUser, DjangoModelPermissions


class RoomUserWritePermission(BasePermission):
    message = 'Editing rooms is restricted to the host only.'

    def has_object_permission(self, request, view, obj):

        if request.method in SAFE_METHODS:
            return True

        return obj.host == request.username


class RoomList(generics.ListCreateAPIView):
    # permission_class = [DjangoModelPermissions]
    permission_class = (IsAuthenticated,)
    queryset = Room.objects.all()
    serializer_class = RoomSerializer

class RoomInside(generics.RetrieveUpdateDestroyAPIView, RoomUserWritePermission):

    permission_class = (RoomUserWritePermission,)
    # permission_class = (IsAuthenticated,)
    queryset = Room.objects.all()
    serializer_class = RoomSerializer

class CategoryList(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

