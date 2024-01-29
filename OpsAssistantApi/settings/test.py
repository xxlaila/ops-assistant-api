'''
@File    ：test.py
@IDE     ：PyCharm 
@Author  ：xxlaila
@Time    ：2024/1/29 18:04 
'''

import os
from .base import *
from pathlib import Path

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://127.0.0.1:6379/8",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
            "CONNECTION_POOL_KWARGS": {"max_connections": 100},
            "COMPRESSOR": "django_redis.compressors.zlib.ZlibCompressor",
            "IGNORE_EXCEPTIONS": True,
            "PASSWORD": "",
        }
    }
}

CELERY_CONFIG = {
    "BROKER_URL": 'redis://127.0.0.1:6379/8',
    "RESULT_BACKEND": 'redis://127.0.0.1:6379/8'
}