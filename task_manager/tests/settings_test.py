"""
Test settings for Django tests
"""

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent

SECRET_KEY = 'django-insecure-test-key-for-running-tests-only'

DEBUG = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
    }
}

ROLLBAR = {
    'access_token': 'test_token',
    'environment': 'test',
    'code_version': '1.0',
    'root': BASE_DIR,
}

# Import all other settings from the main settings file
# This should be at the end of the file so that overrides above take precedence
from task_manager.settings import *  # noqa F403 