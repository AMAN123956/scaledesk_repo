from rest_framework import generics

from suser.models import *
from .serializers import UserSerializer , DesgSerializer

class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class Userupdate(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class Userreti(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class DesListView(generics.ListAPIView):
    queryset = Desgniation.objects.all()
    serializer_class = DesgSerializer

class Desupdate(generics.CreateAPIView):
    queryset = Desgniation.objects.all()
    serializer_class = DesgSerializer

class Desreti(generics.RetrieveUpdateDestroyAPIView):
    queryset = Desgniation.objects.all()
    serializer_class = DesgSerializer