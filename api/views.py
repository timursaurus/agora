from rest_framework.response import Response
from rest_framework import generics
from . models import Room
from . serializers import RoomSerializer

# Create your views here.

class RoomView(generics.RetrieveAPIView):
    queryset = Room.objects.all()

    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = RoomSerializer(queryset, many=True)
        return Response(serializer.data)


