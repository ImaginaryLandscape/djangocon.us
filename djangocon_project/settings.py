# -*- coding: utf-8 -*-
# Django settings for account project

import os.path
import posixpath

PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
DEPLOYMENT_ROOT = os.path.join(PROJECT_ROOT, '..', '..', '..')

DEBUG = True
TEMPLATE_DEBUG = DEBUG

DEFAULT_FROM_EMAIL = "webmaster@djangocon.us"

# tells Pinax to serve media through the staticfiles app.
SERVE_MEDIA = DEBUG

# django-compressor is turned off by default due to deployment overhead for
# most users. See <URL> for more information
#COMPRESS = False

COMPRESS_ENABLED = True
COMPRESS_OUTPUT_DIR = ''
COMPRESS_PRECOMPILERS = (
    ('text/x-sass', '/usr/bin/sass {infile} {outfile}'),
    ('text/x-scss', '/usr/bin/sass --scss {infile} {outfile}'),
    ('text/less', 'lessc {infile} {outfile}'),
)
COMPRESS_CSS_FILTERS = [
    'compressor.filters.cssmin.CSSMinFilter'
]
COMPRESS_JS_FILTERS = [
    'compressor.filters.jsmin.JSMinFilter'
]


INTERNAL_IPS = [
    "127.0.0.1",
]

ADMINS = [
     ("Test", "test.imaginary@gmail.com"),
]

MANAGERS = ADMINS

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3", # Add "postgresql_psycopg2", "postgresql", "mysql", "sqlite3" or "oracle".
        "NAME": "dev.db",                       # Or path to database file if using sqlite3.
        "USER": "",                             # Not used with sqlite3.
        "PASSWORD": "",                         # Not used with sqlite3.
        "HOST": "",                             # Set to empty string for localhost. Not used with sqlite3.
        "PORT": "",                             # Set to empty string for default. Not used with sqlite3.
    }
}

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = "US/Eastern"

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = "en-us"

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = False

ugettext = lambda s: s

LANGUAGES = (
    ('en', u'English'),
)

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = os.path.join(DEPLOYMENT_ROOT, 'htdocs', 'media')

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = '/media/'

# Absolute path to the directory that holds static files like app media.
# Example: "/home/media/media.lawrence.com/apps/"
STATIC_ROOT = os.path.join(DEPLOYMENT_ROOT, "htdocs", "static")

# URL that handles the static files like app media.
# Example: "http://media.lawrence.com"
STATIC_URL = "/static/"

# Additional locations of static files
STATICFILES_DIRS = (
    os.path.join(PROJECT_ROOT, 'static'),
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    "staticfiles.finders.FileSystemFinder",
    "staticfiles.finders.AppDirectoriesFinder",
    "staticfiles.finders.LegacyAppDirectoriesFinder",
    "compressor.finders.CompressorFinder",
)

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = posixpath.join(STATIC_URL, "admin/")

# Make this unique, and don't share it with anybody.
SECRET_KEY = "2(e@(*+ykqa_)%cl-rzw6#4ah2by=d=f^+l9s1@^jlpnfuqp%e"

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = [
    "django.template.loaders.filesystem.load_template_source",
    "django.template.loaders.app_directories.load_template_source",
]

MIDDLEWARE_CLASSES = [
    "django.middleware.common.CommonMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django_openid.consumer.SessionConsumer",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.contrib.flatpages.middleware.FlatpageFallbackMiddleware",
    "pinax.apps.account.middleware.LocaleMiddleware",
    "pinax.middleware.security.HideSensistiveFieldsMiddleware",
    "debug_toolbar.middleware.DebugToolbarMiddleware",
]

ROOT_URLCONF = "djangocon_project.urls"

TEMPLATE_DIRS = [
    os.path.join(PROJECT_ROOT, "templates"),
]

TEMPLATE_CONTEXT_PROCESSORS = [
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.core.context_processors.request",
    "django.contrib.messages.context_processors.messages",

    'photologueext.context_processors.media',

    "pinax.core.context_processors.pinax_settings",

    "pinax.apps.account.context_processors.account",
]

FILE_UPLOAD_HANDLERS = (
    'photologueext.uploadhandler.UploadProgressCachedHandler',
    'django.core.files.uploadhandler.MemoryFileUploadHandler',
    'django.core.files.uploadhandler.TemporaryFileUploadHandler',
)

INSTALLED_APPS = [
    # Django
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.sites",
    "django.contrib.messages",
    "django.contrib.humanize",
    "django.contrib.flatpages",
    # 'django.contrib.staticfiles',

    "pinax.templatetags",

    # theme
    "pinax_theme_bootstrap",

    # external
    "compressor",
    "debug_toolbar",
    "mailer",
    "django_openid",
    "timezones",
    "emailconfirmation",
    "biblion",
    "sorl.thumbnail",
    "metron",
    "gunicorn",
    "photologueext",
    "photologue",
    "staticfiles",
    "uni_form",
    "ajax_validation",
    "markitup",

    # Pinax
    "pinax.apps.account",
    "pinax.apps.signup_codes",

    # symposion
    "symposion.conference",
    "symposion.speakers",
    "symposion.review",
    "symposion.schedule",
    "symposion.proposals",

    # project
    "sponsors", #custom project version
]

FIXTURE_DIRS = [
    os.path.join(PROJECT_ROOT, "fixtures"),
]

MESSAGE_STORAGE = "django.contrib.messages.storage.session.SessionStorage"

#EMAIL_BACKEND = "mailer.backend.DbBackend"
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"

PHOTOLOGUEEXT_DISABLE_WATERMARKS = True
PHOTOLOGUEEXT_M2M_THUMBNAILS = True
PHOTOLOGUEEXT_ONE_GALLERY_PER_PHOTO = True

ACCOUNT_OPEN_SIGNUP = True
ACCOUNT_REQUIRED_EMAIL = False
ACCOUNT_EMAIL_VERIFICATION = False
ACCOUNT_EMAIL_AUTHENTICATION = False
ACCOUNT_UNIQUE_EMAIL = EMAIL_CONFIRMATION_UNIQUE_EMAIL = False

AUTHENTICATION_BACKENDS = [
    "pinax.apps.account.auth_backends.AuthenticationBackend",
]

REDIS_PARAMS = dict(host="127.0.0.1")

MARKITUP_AUTO_PREVIEW = True
MARKITUP_SET = "markitup/sets/markdown-custom"
MARKITUP_SKIN = "markitup/skins/simple"
#MARKITUP_FILTER = ("wiki.markdown_parser.parse", {})
#MARKITUP_FILTER = ("wiki.markdown_parser", {})
#MARKITUP_FILTER = ('django.contrib.markup.templatetags.markup.textile', {})
MARKITUP_FILTER = ("markdown.markdown", {"safe_mode": True})

MARKITUP_MEDIA_URL = STATIC_URL

LOGIN_URL = "/account/login/" # @@@ any way this can be a url name?
LOGIN_REDIRECT_URLNAME = "what_next"

EMAIL_CONFIRMATION_DAYS = 2
EMAIL_DEBUG = DEBUG

DEBUG_TOOLBAR_CONFIG = {
    "INTERCEPT_REDIRECTS": False,
}

THUMBNAIL_EXTENSION = "PNG"

ACCEPTING_PROPOSALS = True
SCHEDULE_TIMEZONE = "US/Pacific"

# local_settings.py can be used to override environment-specific settings
# like database and email that differ between development and production.
try:
    from local_settings import *
except ImportError:
    pass
