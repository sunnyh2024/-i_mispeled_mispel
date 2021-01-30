from .models import Room
from .serializers import RoomSerializer
from rest_framework import generics 

# Create your views here.
class RoomView(generics.CreateAPIView):  
  queryset = Room.objects.all()
  serializer_class = RoomSerializer 

 

