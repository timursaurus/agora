from rest_framework import serializers
from . models import Room, Category

class RoomSerializer(serializers.ModelSerializer):

    # category_name = serializers.ReadOnlyField()
    # host_name = serializers.ReadOnlyField()
    category_name = serializers.ReadOnlyField(source='category.name')
    host_name = serializers.ReadOnlyField(source='host.username')
    class Meta:
        model = Room
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class CreateRoom(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'
        