from rest_framework import serializers
from suser.models import *

class UserSerializer(serializers.ModelSerializer):
   class Meta:
       model = User
       fields = "__all__"

