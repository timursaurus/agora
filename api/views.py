from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import generics
from . models import Room, Category
from . serializers import RoomSerializer, CategorySerializer
from rest_framework import permissions, filters
from rest_framework.exceptions import PermissionDenied
from users.models import User
from users.serializers import UserSerializer
import django_filters
# import SAFE_METHODS, IsAuthenticated, IsAuthenticatedOrReadOnly, BasePermission, IsAdminUser, DjangoModelPermissions


class isHost(permissions.BasePermission):
    message = 'You can\'t edit someone\'s else room lol'
    def has_object_permission(self, request, view, obj):
        return obj.host == request.user

class RoomFilter(django_filters.FilterSet):
    # categories = CharFilterInFilter(field_name='category_name', )
    class Meta:
        model = Room
        fields = '__all__'


class CreateRoom(generics.CreateAPIView):
    permission_class = permissions.IsAuthenticated
    queryset = Room.objects.all()
    serializer_class = RoomSerializer


class EditRoom(generics.RetrieveUpdateDestroyAPIView, isHost):
    permission_classes = (isHost, permissions.IsAuthenticated)
    queryset = Room.objects.all()
    serializer_class = RoomSerializer


class RoomList(generics.ListAPIView):
    # permission_class = [DjangoModelPermissions]
    permission_class = permissions.IsAuthenticatedOrReadOnly
    queryset = Room.objects.all()
    serializer_class = RoomSerializer

    catFilter = RoomFilter()
    filter_backends = [filters.SearchFilter]
    search_fields = ['^title']
    # def get_queryset(self):
    #     queryset = Room.objects.all()
    #     params = self.request.query_params
    #     category = params.get('category_name', None)
    #     if category:
    #         queryset = queryset.filter(category_name = category)
    

class RoomInside(generics.RetrieveAPIView):
    permission_class = permissions.IsAuthenticated
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    
class CategoryList(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filter_backends = [filters.SearchFilter,]
    search_fields = ['^name']

class UserList(generics.ListAPIView):
    permission_class = permissions.IsAuthenticatedOrReadOnly
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['^username']