import os
from pathlib import Path
from datetime import timedelta



def load_env_file(path):
    """Load simple KEY=value entries without requiring python-dotenv."""
    if not path.is_file():
        return

    for line in path.read_text().splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        value = value.strip().strip('"').strip("'")
        os.environ.setdefault(key.strip(), value)


BASE_DIR = Path(__file__).resolve().parent.parent

load_env_file(BASE_DIR.parent / ".env")


SECRET_KEY = os.getenv(
    "SECRET_KEY",
    "greencheck-secret-key-change"
)


DEBUG = True


ALLOWED_HOSTS = [
    "*"
]


# Applications Django

INSTALLED_APPS = [

    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    "rest_framework",
    "rest_framework_simplejwt",

    "corsheaders",

    "dashboard",
    "accounts",
    "identification",
    "plants",
    "diagnostics",

]


# Middleware

MIDDLEWARE = [

    "corsheaders.middleware.CorsMiddleware",

    "django.middleware.security.SecurityMiddleware",

    "django.contrib.sessions.middleware.SessionMiddleware",

    "django.middleware.common.CommonMiddleware",

    "django.middleware.csrf.CsrfViewMiddleware",

    "django.contrib.auth.middleware.AuthenticationMiddleware",

    "django.contrib.messages.middleware.MessageMiddleware",

    "django.middleware.clickjacking.XFrameOptionsMiddleware",

]


# URL principale

ROOT_URLCONF = "config.urls"


# Templates

TEMPLATES = [

    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",

        "DIRS": [
            BASE_DIR / "templates"
        ],

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


# WSGI

WSGI_APPLICATION = "config.wsgi.application"


# Base PostgreSQL Docker

DATABASES = {

    "default": {

        "ENGINE": "django.db.backends.postgresql",

        "NAME": os.getenv(
            "DATABASE_NAME",
            "greencheck"
        ),

        "USER": os.getenv(
            "DATABASE_USER",
            "greencheck"
        ),

        "PASSWORD": os.getenv(
            "DATABASE_PASSWORD",
            "greencheck_password"
        ),

        "HOST": os.getenv(
            "DATABASE_HOST",
            "postgres"
        ),

        "PORT": os.getenv(
            "DATABASE_PORT",
            "5432"
        ),

    }

}



# Validation mots de passe

AUTH_PASSWORD_VALIDATORS = []



# Langue

LANGUAGE_CODE = "fr-fr"

TIME_ZONE = "Europe/Paris"

USE_I18N = True

USE_TZ = True



# Static

STATIC_URL = "/static/"

STATIC_ROOT = BASE_DIR / "staticfiles"



# Media

MEDIA_URL = "/media/"

MEDIA_ROOT = BASE_DIR / "media"



# DRF

REST_FRAMEWORK = {

    "DEFAULT_AUTHENTICATION_CLASSES": (

        "rest_framework_simplejwt.authentication.JWTAuthentication",

    ),

}

SIMPLE_JWT = {

    "ACCESS_TOKEN_LIFETIME":
        timedelta(minutes=60),

    "REFRESH_TOKEN_LIFETIME":
        timedelta(days=7),

}

SPECTACULAR_SETTINGS = {

    "TITLE":
    "GreenCheck API",


    "DESCRIPTION":
    "API catalogue plantes et maladies IA",


    "VERSION":
    "1.0.0"

}



# CORS React

CORS_ALLOWED_ORIGINS = [

    "http://localhost:5173",

]



# Service IA FastAPI

AI_SERVICE_URL = os.getenv(
    "AI_SERVICE_URL",
    "http://ai-service:8001"
)



DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"