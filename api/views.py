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
    permission_class = [DjangoModelPermissions]
    queryset = Room.objects.all()
    serializer_class = RoomSerializer

class RoomInside(generics.RetrieveUpdateDestroyAPIView, RoomUserWritePermission):
    permission_class = [RoomUserWritePermission]
    queryset = Room.objects.all()
    serializer_class = RoomSerializer

class CategoryList(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


# @api_view(['GET'])
# def APIOverview(request):
#     api_urls = {
#         'Rooms': '/rooms/',
#         'Create': '/create/',
#         'Update': '/update/<str:pk>/',
#         'Delete': '/delete/<str:pk>/',
#     }
#     return Response(api_urls)

# @api_view(['GET'])
# def Rooms(request):
#     rooms = Room.objects.all()
#     serializer = RoomSerializer(rooms, many=True)
#     return Response(serializer.data)

# @api_view(['GET'])
# def InsideRoom(request, pk):
#     room = Room.objects.get(id=pk)
#     serializer = RoomSerializer(room, many=False)
#     return Response(serializer.data)

# @api_view(['POST'])
# def CreateRoom(request):
#     serializer = RoomSerializer(data=request.data)
#     return Response(serializer.data)

#     if serializer.is_valid():
#         serializer.save()

# @api_view(['POST'])
# def UpdateRoom(request):
#     room = Room.objects.get(id=pk)
#     serializer = RoomSerializer(instance=room ,data=request.data)
#     return Response(serializer.data)

#     if serializer.is_valid():
#         serializer.save()


# @api_view(['DELETE'])
# def DeleteRoom(request):
#     room = Room.objects.get(id=pk)
#     room.delete()

#     return Response('Room ended')



# Create your views here.

# class RoomView(generics.RetrieveAPIView):
#     queryset = Room.objects.all()

#     def get(self, request, *args, **kwargs):
#         queryset = self.get_queryset()
#         serializer = RoomSerializer(queryset, many=True)
#         return Response(serializer.data)


# class CreateRoomView(APIView):
#     serializer_class = CreateRoomSerializer

#     def post(self, request, format=None):


#         if not self.request.session.exists(self.request.session.session_key):
#             self.request.create()

#         serializer = self.serializer_class(data=request.data)
#         if serializer.is_valid():
#             host = self.request.session.session_key
#             title = serializer.data.get('title')
#             private = serializer.data.get('private')
#             description = serializer.data.get('description')
#             queryset = Room.objects.filter(host=host)
#             if queryset.exists():
#                 pass
#             else:
#                 room = Room(host=host, title=title, description=description, private=private)
#                 room.save()
#             return Response(RoomSerializer(room).data, status=status.HTTP_201_CREATED)

