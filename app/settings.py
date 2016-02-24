import os
import datetime
from celery.schedules import crontab
from kombu import (
    Queue,
    Exchange,
    )

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SECRET_KEY = os.environ['SECRET_KEY']
DEBUG = True
ALLOWED_HOSTS = []
INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'django_extensions',
    'social.apps.django_app.default',
    'kombu.transport.django',
    'celery',
    'blog',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    # 'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'rewritebody.django.RwriteBodyMiddleware',
)

ROOT_URLCONF = 'app.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'social.apps.django_app.context_processors.backends',
                'social.apps.django_app.context_processors.login_redirect',
            ],
        },
    },
]

WSGI_APPLICATION = 'app.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'HOST': os.environ['DATABASE_DEFAULT_HOST'],
        'PORT': os.environ['DATABASE_DEFAULT_PORT'],
        'NAME': os.environ['DATABASE_DEFAULT_NAME'],
        'USER': os.environ['DATABASE_DEFAULT_USER'],
        'PASSWORD': os.environ['DATABASE_DEFAULT_PASSWORD'],
    }
}


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'ja'

TIME_ZONE = 'Asia/Tokyo'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

# for celery
CELERY_TIMEZONE = TIME_ZONE
BROKER_URL = os.environ['BROKER_URL']
CELERY_RESULT_BACKEND = os.environ['CELERY_RESULT_BACKEND']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_ACCEPT_CONTENT = ['json']
CELERY_ALWAYS_EAGER = False
CELERY_SEND_EVENTS = True
CELERY_SEND_TASK_SENT_EVENT = True
CELERY_ENABLE_UTC = False
CELERY_ACKS_LATE = True
CELERYD_PREFETCH_MULTIPLIER = 1
BROKER_TRANSPORT_OPTIONS = {'fanout_patterns': True, 'visibility_timeout': 10 * 60}
CELERY_TASK_RESULT_EXPIRES = 18000
CELERYD_HIJACK_ROOT_LOGGER = False
CELERYD_LOG_FORMAT = "%(asctime)s\t%(levelname)s\t%(processName)s\t%(message)s"
CELERYD_TASK_LOG_FORMAT = "%(asctime)s\t%(levelname)s\t%(processName)s\t%(task_name)s\t%(task_id)s\t%(message)s"  # noqa
CELERY_DISABLE_RATE_LIMITS = True

# for celery beat
CELERYBEAT_SCHEDULE = {
    'debug_task': {
        'task': 'app.celery.debug_task',
        'schedule': crontab(minute='*/2'),
        'args': (),
    },
}

# for celery routing
CELERY_QUEUES = [
    Queue('default', Exchange('default', type='direct'), routing_key='default'),
    Queue('debug', Exchange('debug', type='direct'), routing_key='debug'),
]
CELERY_DEFAULT_QUEUE = 'default'
CELERY_DEFAULT_EXCHANGE = 'default'
CELERY_DEFAULT_ROUTING_KEY = 'default'
CELERY_ROUTERS = [{
    'app.celery.debug_task': {
        'queue': 'debug',
        'routing_key': 'debug',
    },
}]


# for celery once
ONCE_REDIS_URL = os.environ['ONCE_REDIS_URL']
ONCE_DEFAULT_TIMEOUT = 10

# for requests
VERIFY_SSL = False if DEBUG else True

# for rewritebody
REWRITEBODY_PAIRS = [
    (b'</body>', os.environ.get('ENV_TAG', '').encode()),  # noqa
]

# for rst_framework
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
    ),
}

# for jwt
JWT_AUTH = {
    'JWT_ENCODE_HANDLER': 'rest_framework_jwt.utils.jwt_encode_handler',
    'JWT_DECODE_HANDLER': 'rest_framework_jwt.utils.jwt_decode_handler',
    'JWT_PAYLOAD_HANDLER': 'rest_framework_jwt.utils.jwt_payload_handler',
    'JWT_PAYLOAD_GET_USER_ID_HANDLER': 'rest_framework_jwt.utils.jwt_get_user_id_from_payload_handler',  # noqa
    'JWT_RESPONSE_PAYLOAD_HANDLER': 'rest_framework_jwt.utils.jwt_response_payload_handler',
    'JWT_SECRET_KEY': SECRET_KEY,
    'JWT_ALGORITHM': 'HS256',
    'JWT_VERIFY': True,
    'JWT_VERIFY_EXPIRATION': True,
    'JWT_LEEWAY': 0,
    'JWT_EXPIRATION_DELTA': datetime.timedelta(seconds=300),
    'JWT_AUDIENCE': None,
    'JWT_ISSUER': None,
    'JWT_ALLOW_REFRESH': False,
    'JWT_REFRESH_EXPIRATION_DELTA': datetime.timedelta(days=7),
    'JWT_AUTH_HEADER_PREFIX': 'JWT',
}

# for authentication
AUTHENTICATION_BACKENDS = [
    'social.backends.google.GoogleOAuth2',
    'django.contrib.auth.backends.ModelBackend',
]

# for social auth
SOCIAL_AUTH_RAISE_EXCEPIONS = True
RAISE_EXCEPTION = True

SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = \
    os.environ['SOCIAL_AUTH_GOOGLE_OAUTH2_KEY']
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = \
    os.environ['SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET']

SOCIAL_AUTH_UID_LENGTH = 223
SOCIAL_AUTH_LOGIN_ERROR_URL = '/'
SOCIAL_AUTH_GOOGLE_OAUTH2_WHITELISTED_EMAILS = \
    os.environ.get('SOCIAL_AUTH_GOOGLE_OAUTH2_WHITELISTED_EMAILS', '').split(',')
SOCIAL_AUTH_GOOGLE_OAUTH2_WHITELISTED_DOMAINS = \
    os.environ.get('SOCIAL_AUTH_GOOGLE_OAUTH2_WHITELISTED_DOMAINS', '').split(',')
SOCIAL_AUTH_PIPELINE = (
    'social.pipeline.social_auth.social_details',
    'social.pipeline.social_auth.social_uid',
    'social.pipeline.social_auth.auth_allowed',
    'social.pipeline.social_auth.social_user',
    'social.pipeline.user.get_username',
    'social.pipeline.user.create_user',
    'social.pipeline.social_auth.associate_user',
    'social.pipeline.social_auth.load_extra_data',
    'social.pipeline.user.user_details',
    'app.default_pipline',
)

VERIFY_SSL = False if DEBUG else True

# for reverse proxy
USE_X_FORWARDED_HOST = True
