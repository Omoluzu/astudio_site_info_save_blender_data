from rest_framework import generics
from .models import BlenderPathProject
from .serializers import BlenderPathProjectSerializer


class BlenderPathProjectList(generics.ListCreateAPIView):
    queryset = BlenderPathProject.objects.all()
    serializer_class = BlenderPathProjectSerializer
