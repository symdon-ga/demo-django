"""
Django settings for service_web project.

Generated by 'django-admin startproject' using Django 3.0b1.

For more information on this file, see
https://docs.djangoproject.com/en/dev/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/dev/ref/settings/
"""
import os
import pathlib
import dotenv

DOTENV = os.environ.get('DOTENV')
if DOTENV:
    dotenv.load_dotenv(DOTENV)

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
settings_path = pathlib.Path(__file__).resolve()
# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
HERE = settings_path.parents[0]
BASE_DIR = settings_path.parents[1]

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/dev/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ["SYMDON_DJANGO_SECRET_KEY"]

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get("SYMDON_DJANGO_MODE", "DEBUG") == "DEBUG"

ALLOWED_HOSTS = [
    "127.0.0.1",
    "localhost",
    os.environ.get("SYMDON_DJANGO_HOST"),
]


# Application definition

INSTALLED_APPS = [
    # default
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # customize
    # original
    'apps.symdon_auth',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'service_web.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            (HERE / "templates"),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'service_web.wsgi.application'


# Database
# https://docs.djangoproject.com/en/dev/ref/settings/#databases

database_type = os.environ.get("SYMDON_DJANGO_DATABASE_TYPE", "sqlite3")
if database_type == "sqlite3":
    DATABASES = {
        'default': {
            'ENGINE': os.environ.get("SYMDON_DJANGO_DATABASE_ENGINE", f"django.db.backends.{database_type}"),
            'NAME': os.environ.get("SYMDON_DJANGO_DATABASE_NAME", os.path.join(BASE_DIR, 'db.sqlite3')),
        }
    }
elif database_type == "mysql":
    DATABASES = {
        'default': {
            'ENGINE': os.environ.get("SYMDON_DJANGO_DATABASE_ENGINE", f"django.db.backends.{database_type}"),
            'HOST': os.environ.get("SYMDON_DJANGO_DATABASE_HOST", "127.0.0.1"),
            'NAME': os.environ.get("SYMDON_DJANGO_DATABASE_NAME", "symdon_django"),
            'PASSWORD': os.environ.get("SYMDON_DJANGO_DATABASE_PASSWORD", ""),
            'PORT': os.environ.get("SYMDON_DJANGO_DATABASE_PORT", "3306"),
            'USER': os.environ.get("SYMDON_DJANGO_DATABASE_USER", "root"),
        }
    }
else:
    assert False, f"Unsupport database type: {database_type}"

# Password validation
# https://docs.djangoproject.com/en/dev/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/dev/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/dev/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(
    os.environ.get("SYMDON_DJANGO_STATIC_ROOT") or (BASE_DIR / "dist"),
    "static",
)

SYMDON_AUTH_CLIENT_ID = "symdon-django"
SYMDON_AUTH_REALM = "demo"
SYMDON_AUTH_REDIRECT_URI = os.environ.get("SYMDON_DJANGO_SYMDON_AUTH_REDIRECT_URI",
                                          "https://localhost:8000/callback/")
SYMDON_AUTH_AUTH_URL = "https://auth.symdon.ga/auth/realms/demo/protocol/openid-connect/auth"



