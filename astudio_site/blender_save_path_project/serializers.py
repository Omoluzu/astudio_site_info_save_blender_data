from rest_framework import serializers
from .models import BlenderPathProject


class BlenderPathProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlenderPathProject
        fields = ['author', 'time_save_project', 'path_save_project']
