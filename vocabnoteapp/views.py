
# Create your views here.


from rest_framework import generics
from .models import  User
from vocabnoteapp.serializers import Usererializer

# Create your views here.
class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = Usererializer
