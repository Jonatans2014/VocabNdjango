
# Create your views here.


from rest_framework import generics
from  .models import User
from .serializers import UserSerializer

# Create your views here.


#User list of create another one
#Users/

class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

