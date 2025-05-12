from task_manager.settings import *

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