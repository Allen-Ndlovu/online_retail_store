import os
from pathlib import Path

# Build paths inside the project
BASE_DIR = Path(__file__).resolve().parent.parent

# Import custom configuration; fall back to defaults if not present.
try:
    from backend.online_retail_store.config import DATABASES_CONFIG, SECRET_KEY_CONFIG, DEBUG_CONFIG, ALLOWED_HOSTS_CONFIG
except ImportError:
    DATABASES_CONFIG = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': os.environ.get('DB_NAME', 'onlineretaildb'),
            'USER': os.environ.get('DB_USER', 'your_username'),
            'PASSWORD': os.environ.get('DB_PASSWORD', 'your_password'),
            'HOST': os.environ.get('DB_HOST', 'localhost'),
            'PORT': os.environ.get('DB_PORT', '5432'),
        }
    }
    SECRET_KEY_CONFIG = os.environ.get('DJANGO_SECRET_KEY', 'your_default_secret_key')
    DEBUG_CONFIG = os.environ.get('DJANGO_DEBUG', 'True') == 'True'
    ALLOWED_HOSTS_CONFIG = os.environ.get('DJANGO_ALLOWED_HOSTS', 'localhost').split(',')

SECRET_KEY = SECRET_KEY_CONFIG
DEBUG = DEBUG_CONFIG
ALLOWED_HOSTS = ALLOWED_HOSTS_CONFIG

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'corsheaders',
    'products',
    'orders',
    'users',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',  # Allow cross-origin requests
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# Allow all origins for development (change for production)
CORS_ALLOW_ALL_ORIGINS = True

ROOT_URLCONF = 'online_retail_store.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / "templates"],
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

WSGI_APPLICATION = 'online_retail_store.wsgi.application'

DATABASES = DATABASES_CONFIG

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    # Additional validators can be added here
]

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / "static"]

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.AllowAny',
    ],
}
