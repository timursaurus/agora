from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class BaseModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    class Meta:
        abstract = True


class Room(BaseModel):
    title = models.CharField(max_length=255)
    host = models.ForeignKey(User, on_delete=models.CASCADE, related_name='room_host')
    private = models.BooleanField(null= False, default = False)
    description = models.TextField(blank=True)

    class Meta:
        verbose_name_plural = 'Rooms'

    def __str__(self):
        return self.title


#class Listener(models.Model):
    #room = models.ForeignKey(Room, on_delete=models.PROTECT)
    #listeners = models.ManyToManyField(User,on_delete=models.CASCADE)


#class Speaker(models.Model):
    #room = models.ForeignKey(Room, on_delete=models.PROTECT)
    #speakers = models.ManyToManyField(User, on_delete=models.CASCADE)
    