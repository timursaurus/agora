from django.db import models
from django.contrib.auth.models import User
import uuid, string, random
from django.conf import settings
from django.db.models.deletion import SET_NULL

def gencode():
    k = 8
    while True:
        code = ''.join(random.choices(string.ascii_uppercase, k=k))
        if Room.objects.filter(code=code).count() == 0:
            break

    return code


class BaseModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    class Meta:
        abstract = True


class Category(BaseModel):
    name = models.CharField(max_length=50)
    
    class Meta:
        verbose_name_plural = 'Categories'
        verbose_name = 'Category'

    def __str__(self):
        return self.name



class Room(BaseModel):

    options = (
        ('public', 'Public'),
        ('private', 'Private')
    )

    class PublicRooms(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter(privacy='public')

    

    title = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, default='')
    host = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='room_host')
    privacy = models.CharField(max_length=10, choices=options, default='public')
    description = models.TextField(blank=True)
    code = models.CharField(primary_key=True, max_length=8, default=gencode , unique=True)
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    objects = models.Manager()
    public_rooms = PublicRooms()

    class Meta:
        verbose_name_plural = 'Rooms'
        verbose_name = 'Room'

    def __str__(self):
        return self.title
    
    # def host_name(self):
    #     return self.host_name

    # def category_name(self):
    #     return self.category_name


   
