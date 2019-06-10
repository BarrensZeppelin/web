"""
Django settings for fredagscafeen project.

Generated by 'django-admin startproject' using Django 1.8.5.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!

MAILMAN_URL_BASE = 'https://maillist.au.dk/mailman'
MAILMAN_ALL_LIST = 'datcafe-alle.cs'
MAILMAN_BEST_LIST = 'datcafe-best.cs'

SECRET_ADMIN_KEYS = [
	('SECRET_KEY', 'Django secret key', None),
	('MAILMAN_ALL_PASSWORD', 'Alle mailinglist admin password', f'{MAILMAN_URL_BASE}/admin/{MAILMAN_ALL_LIST}'),
	('MAILMAN_BEST_PASSWORD', 'Best mailinglist admin password', f'{MAILMAN_URL_BASE}/admin/{MAILMAN_BEST_LIST}'),
	('EMAIL_HOST_PASSWORD', 'Gmail password', 'https://gmail.com/'),
	('DIGITAL_OCEAN_PASSWORD', 'Digital Ocean password', 'https://cloud.digitalocean.com/login'),
	('MIDTTRAFIK_BESTILLING_PASSWORD', 'midttrafikbestilling.dk password', 'https://midttrafikbestilling.dk/'),
	('RECAPTCHA_PRIVATE_KEY', 'ReCaptcha private key', None),
]

CONSTANCE_CONFIG = {
	'REGISTRATION_OPEN': (True, 'Er bartendertilmelding åben?', bool),
}

# Inject all secret keys
for k, _, _ in SECRET_ADMIN_KEYS:
	v = os.getenv(k)
	if v != None:
		globals()[k] = v
	else:
		print('WARNING: Missing secret key in env:', k)


BOOTSTRAP3 = {
	'success_css_class': '',
}


# SECURITY WARNING: don't run with debug turned on in production!

# ALLOWED_HOSTS = ['*']

# Application definition

INSTALLED_APPS = (
	'admin_views',
	'django.contrib.admin',
	'django.contrib.auth',
	'django.contrib.contenttypes',
	'django.contrib.sessions',
	'django.contrib.messages',
	'django.contrib.staticfiles',
	'django_object_actions',
	'django_extensions',
	'constance',
	'constance.backends.database',
	'rest_framework.authtoken',
	'bootstrap3',
	'bootstrap_datepicker_plus',
	'captcha',
	'rest_framework',
	'corsheaders',
	'items',
	'bartenders',
	'web',
	'api',
	'reminder',
	'udlejning',
	'logentry_admin',
	'bartab',
	'email_auth',
	'guides',
	'events',
)

MIDDLEWARE = (
	'django.middleware.security.SecurityMiddleware',
	'whitenoise.middleware.WhiteNoiseMiddleware',
	'django.contrib.sessions.middleware.SessionMiddleware',
	'corsheaders.middleware.CorsMiddleware',
	'django.middleware.common.CommonMiddleware',
	'django.middleware.csrf.CsrfViewMiddleware',
	'django.contrib.auth.middleware.AuthenticationMiddleware',
	'django.contrib.messages.middleware.MessageMiddleware',
	'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

AUTHENTICATION_BACKENDS = (
	'django.contrib.auth.backends.ModelBackend',
	'email_auth.auth.EmailTokenBackend',
)

REST_FRAMEWORK = {
	'DEFAULT_AUTHENTICATION_CLASSES': (
		'rest_framework.authentication.TokenAuthentication',
		'rest_framework.authentication.BasicAuthentication',
		'rest_framework.authentication.SessionAuthentication',
	),
	'DEFAULT_PERMISSION_CLASSES': (
		'rest_framework.permissions.IsAuthenticatedOrReadOnly',
		'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly',
	)
}

ROOT_URLCONF = 'fredagscafeen.urls'

TEMPLATES = [
	{
		'BACKEND': 'django.template.backends.django.DjangoTemplates',
		'DIRS': ['web/templates', 'fredagscafeen/templates'],
		'APP_DIRS': True,
		'OPTIONS': {
			'context_processors': [
				'constance.context_processors.config',
				'django.template.context_processors.debug',
				'django.template.context_processors.request',
				'django.contrib.auth.context_processors.auth',
				'django.contrib.messages.context_processors.messages',
			],
		},
	},
]

WSGI_APPLICATION = 'fredagscafeen.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
	'default': {
		'ENGINE': 'django.db.backends.sqlite3',
		'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
	}
}


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'da-DK'

TIME_ZONE = 'Europe/Copenhagen'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles/')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')

LOGIN_URL = '/login/'

# Use the new NoCaptcha
NOCAPTCHA = True

# CORS Setup
CORS_URLS_REGEX = r'^/api/.*$'  # Only allow CORS requests in /api
CORS_ORIGIN_ALLOW_ALL = True

CONSTANCE_BACKEND = 'constance.backends.database.DatabaseBackend'

# Server admins (get an email when server errors happen)
ADMINS = [
	('Oskar Haarklou Veileborg', 'oskarv@post.au.dk'),
	('Asger Hautop Drewsen', 'asgerdrewsen@gmail.com'),
]

# Allow more fields in GET/POST requests (necessary for BarTabAdmin to function with large snapshots)
DATA_UPLOAD_MAX_NUMBER_FIELDS = 10 ** 6

# Session cookie lasts a year
SESSION_COOKIE_AGE = 365 * 24 * 60 * 60
