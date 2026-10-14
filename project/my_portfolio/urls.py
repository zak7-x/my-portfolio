from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),

    # The home page and About page are handled by the about app.
    path("", include("about.urls")),

    # The Projects page is handled by the project app.
    path("projects/", include("project.urls")),

    # The Contact page is handled by the contact app.
    path("contact/", include("contact.urls")),
]
