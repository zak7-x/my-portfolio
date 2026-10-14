from pathlib import Path
import os

from django.template.context_processors import static

# BASE_DIR points to the main folder containing manage.py.
BASE_DIR = Path(__file__).resolve().parent.parent

# Keep this key private if you deploy the website publicly.
# Read the secret key from the server environment.
SECRET_KEY = os.environ.get(
    "DJANGO_SECRET_KEY",
    "django-insecure-local-development-only"
)

# Enable debugging locally, but disable it on the live server.
DEBUG = os.environ.get("DJANGO_DEBUG", "True").lower() == "true"

# Allow local development and any hosts configured on the server.
ALLOWED_HOSTS = [
    host.strip()
    for host in os.environ.get(
        "DJANGO_ALLOWED_HOSTS",
        "localhost,127.0.0.1"
    ).split(",")
    if host.strip()
]

# Django apps that are included in this website.
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "about",
    "project",
    "contact",
]

# Middleware helps Django process each request and response.
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",

    # Serve static files efficiently on the live website.
    "whitenoise.middleware.WhiteNoiseMiddleware",

    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

# This is the main URL configuration file.
ROOT_URLCONF = "my_portfolio.urls"

# Django uses this configuration to find HTML templates.
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        # Look for shared templates in the top-level templates folder.
        "DIRS": [BASE_DIR / "templates"],
        # Also look inside each installed app for its templates.
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

# WSGI is used by some web servers when the site is deployed.
WSGI_APPLICATION = "my_portfolio.wsgi.application"

# SQLite is a simple local database that comes with Django.
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

# Standard password validators for Django's user accounts.
AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

# Default language and time zone.
LANGUAGE_CODE = "en-us"
TIME_ZONE = "Africa/Kigali"
USE_I18N = True
USE_TZ = True

# Django's static URL starts the path used for CSS and images.
# URL prefix used for static files.
STATIC_URL = "static/"

# Folder containing shared CSS, JavaScript, and images.
STATICFILES_DIRS = [BASE_DIR / "static"]

# Folder where Django collects static files for deployment.
STATIC_ROOT = BASE_DIR / "staticfiles"

# Enable compressed static-file storage for production.
STORAGES = {
    "default": {
        "BACKEND": "django.core.files.storage.FileSystemStorage",
    },
    "staticfiles": {
        "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",
    },
}


# The default ID field type for new Django models.
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"



# Send Django errors to the Render logs.
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,

    # This handler prints errors to the console.
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "level": "ERROR",
            "formatter": "verbose",
        },
    },

    # This format includes the error level, time, and message.
    "formatters": {
        "verbose": {
            "format": "{levelname} {asctime} {name}: {message}",
            "style": "{",
        },
    },

    # Log Django request errors, including their tracebacks.
    "loggers": {
        "django.request": {
            "handlers": ["console"],
            "level": "ERROR",
            "propagate": False,
        },
    },
}
