from django.urls import path
from . import views

urlpatterns = [
    # The empty path is the website homepage.
    path("", views.index, name="index"),

    # /about/ opens the About Me page.
    path("about/", views.about, name="about"),
]
