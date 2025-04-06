import json
import os
from pathlib import Path

# Build paths inside the project
BASE_DIR = Path(__file__).resolve().parent.parent

# Load config from config.json
config_path = os.path.join(BASE_DIR, 'online_retail_store', 'config.json')
with open(config_path) as config_file:
    config = json.load(config_file)

SECRET_KEY = config.get("SECRET_KEY", "dummy_key")
DEBUG = config.get("DEBUG", True)

ALLOWED_HOSTS = config.get("ALLOWED_HOSTS", [])

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': config.get("DB_NAME", "onlineretaildb"),
        'USER': config.get("DB_USER", "your_username"),
        'PASSWORD': config.get("DB_PASSWORD", "your_password"),
        'HOST': config.get("DB_HOST", "localhost"),
        'PORT': config.get("DB_PORT", "5432"),
    }
}

# Other settings...
