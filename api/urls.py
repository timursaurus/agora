from django.urls import path, include
from rest_framework import routers
from .views import RoomList, RoomInside, CategoryList


# router = routers.DefaultRouter()

# router.register(r'rooms', views.Rooms)

urlpatterns = [
    path('room/', RoomList.as_view(), name='room-list'),
    path('room/<str:pk>', RoomInside.as_view(), name='room-inside'),
    path('category/', CategoryList.as_view(), name='category-list'),
]


# urlpatterns = [
#     path('', views.APIOverview, name='api-overview'),
#     path('rooms/', views.Rooms, name='rooms-list'),
#     path('room/<str:pk>', views.InsideRoom, name='room'),
#     path('room-create/', views.CreateRoom, name='room-create'),
#     path('room-update/<str:pk>', views.UpdateRoom, name='room-update'),
#     path('room-delete/<str:pk>', views.DeleteRoom, name='room-delete'),
# ]

# urlpatterns = [
#     path('', include(router.urls)),
#     path('api-auth/', include('rest_framework.urls', namespace='etst'))
# ]
