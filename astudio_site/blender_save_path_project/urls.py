from django.urls import path
from .views import BlenderPathProjectList


urlpatterns = [
    path('/', BlenderPathProjectList.as_view())
]
