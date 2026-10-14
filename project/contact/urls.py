from django.urls import path
from . import views

urlpatterns = [
    # /contact/ opens the contact form.
    path("", views.contact, name="contact"),
]
