from django.urls import path
from .views import CreateUser, BlacklistToken

urlpatterns = [
    path('register/', CreateUser.as_view(), name='user-register'),
    path('logout/blacklist/', BlacklistToken.as_view(), name='token-blacklist' )

]