from fredagscafeen.settings.base import *

SECRET_KEY = "This is insecure"
DEBUG = True

SELF_URL = 'http://localhost:8000/'

MAILMAN_MUTABLE = False

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

SILENCED_SYSTEM_CHECKS = ['captcha.recaptcha_test_key_error']
