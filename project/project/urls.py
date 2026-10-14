from django.urls import path
from . import views

urlpatterns = [
    # /projects/ opens the list of projects.
    path("", views.projects, name="projects"),
]
