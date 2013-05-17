# -*- coding: utf-8 -*-
# Django settings for account project

import os.path
import posixpath

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__)))
PACKAGE_ROOT = os.path.abspath(os.path.dirname(__file__))
DEPLOYMENT_ROOT = os.path.join(PROJECT_ROOT, '..', '..', '..')

DEBUG = False
TEMPLATE_DEBUG = DEBUG

DEFAULT_FROM_EMAIL = "webmaster@djangocon.us"

CONTACT_EMAIL = "djangocon@holdenweb.com"

# tells Pinax to serve media through the staticfiles app.
SERVE_MEDIA = DEBUG

# django-compressor is turned off by default due to deployment overhead for
# most users. See <URL> for more information
COMPRESS = False
COMPRESS_OUTPUT_DIR = ''
COMPRESS_PRECOMPILERS = (
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
    ("Dustin Lacewell", "dlacewell@imagescape.com"),
]

MANAGERS = ADMINS

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3", # Add "postgresql_psycopg2", "postgresql", "mysql", "sqlite3" or "oracle".
        "NAME": os.path.join(PROJECT_ROOT, "djcon.sql"), # Or path to database file if using sqlite3.
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
USE_I18N = True

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = os.path.join(DEPLOYMENT_ROOT, "htdocs", "media")

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = "/media/"

# Absolute path to the directory that holds static files like app media.
# Example: "/home/media/media.lawrence.com/apps/"
STATIC_ROOT = os.path.join(DEPLOYMENT_ROOT, "htdocs", "static")

# URL that handles the static files like app media.
# Example: "http://media.lawrence.com"
STATIC_URL = "/static/"

# Additional directories which hold static files
STATICFILES_DIRS = [
    os.path.join(PROJECT_ROOT, "static"),
]

STATICFILES_FINDERS = [
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
    "django.contrib.staticfiles.finders.DefaultStorageFinder",
    "compressor.finders.CompressorFinder",
]

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = posixpath.join(STATIC_URL, "admin/")

# Make this unique, and don't share it with anybody.
SECRET_KEY = "8*br)9@fs!4nzg-imfrsst&oa2udy6z-fqtdk0*e5c1=wn)(t3"

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = [
    "django.template.loaders.filesystem.Loader",
    "django.template.loaders.app_directories.Loader",
]

MIDDLEWARE_CLASSES = [
    "django.middleware.common.CommonMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.transaction.TransactionMiddleware",
    "reversion.middleware.RevisionMiddleware",
    "debug_toolbar.middleware.DebugToolbarMiddleware",
]

ROOT_URLCONF = "djcon.urls"

TEMPLATE_DIRS = [
    os.path.join(PROJECT_ROOT, "templates"),
]

TEMPLATE_CONTEXT_PROCESSORS = [
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.core.context_processors.tz",
    "django.core.context_processors.request",
    "django.contrib.messages.context_processors.messages",
    "pinax_utils.context_processors.settings",
    "account.context_processors.account",
    "photologueext.context_processors.media",
]

INSTALLED_APPS = [
    # Django
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.sites",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.sitemaps",
    "django.contrib.humanize",
    
    'gunicorn',

    # theme
    "pinax_theme_bootstrap_account",
    "pinax_theme_bootstrap",
    "django_forms_bootstrap",
    
    # external
    "south",
    "compressor",
    "debug_toolbar",
    "mailer",
    "timezones",
    "metron",
    "markitup",
    "taggit",
    "reversion",
    "easy_thumbnails",
    "sitetree",
    "account",
    "photologueext",
    "photologue",
    "filer",
#    "wakawaka",
    "newscenter",
    "tinymce",
    
    # symposion
    "symposion",
    "symposion.sponsorship",
    "symposion.conference",
    "symposion.cms",
    "symposion.boxes",
    "symposion.proposals",
    "symposion.reviews",
    "symposion.schedule",        
    "symposion.speakers",
    "symposion.teams",
    
    # project
    "djcon.proposals",
]

PHOTOLOGUEEXT_DISABLE_WATERMARKS = True
PHOTOLOGUEEXT_M2M_THUMBNAILS = True
PHOTOLOGUEEXT_ONE_GALLERY_PER_PHOTO = True

TINYMCE_DEFAULT_CONFIG = {
    'convert_urls': False,
    'theme': "advanced",
    'height': 355,
    'width': 740
}

FIXTURE_DIRS = [
    os.path.join(PROJECT_ROOT, "fixtures"),
]

MESSAGE_STORAGE = "django.contrib.messages.storage.session.SessionStorage"

EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
#EMAIL_BACKEND = "mailer.backend.DbBackend"

ACCOUNT_OPEN_SIGNUP = True
ACCOUNT_USE_OPENID = False
ACCOUNT_REQUIRED_EMAIL = False
ACCOUNT_EMAIL_VERIFICATION = False
ACCOUNT_EMAIL_AUTHENTICATION = False
ACCOUNT_UNIQUE_EMAIL = EMAIL_CONFIRMATION_UNIQUE_EMAIL = False

ACCOUNT_SIGNUP_REDIRECT_URL = "dashboard"
ACCOUNT_LOGIN_REDIRECT_URL = "dashboard"
ACCOUNT_LOGOUT_REDIRECT_URL = "home"
ACCOUNT_USER_DISPLAY = lambda user: user.email

AUTHENTICATION_BACKENDS = [
    # Permissions Backends
    "symposion.teams.backends.TeamPermissionsBackend",
    
    # Auth backends
    "account.auth_backends.EmailAuthenticationBackend",

    'django.contrib.auth.backends.ModelBackend',
    
]

LOGIN_URL = "/account/login/" # @@@ any way this can be a url name?

EMAIL_CONFIRMATION_DAYS = 2
EMAIL_DEBUG = DEBUG

DEBUG_TOOLBAR_CONFIG = {
    "INTERCEPT_REDIRECTS": False,
}

WAKAWAKA_DEFAULT_INDEX = "index"
WAKAWAKA_SLUG_REGEX = r"((\w{2,})(/\w{2,})*)" # allow lower case wiki page names
WAKAWAKA_LOCK_TIMEOUT = 10*60

MARKITUP_FILTER = ("markdown.markdown", {"safe_mode": True})
MARKITUP_SET = "markitup/sets/markdown"
MARKITUP_SKIN = "markitup/skins/simple"

CONFERENCE_ID = 1

SYMPOSION_PAGE_REGEX = r"(([\w-]{1,})(/[\w-]{1,})*)/"

PROPOSAL_FORMS = {
    "tutorial": "djcon.proposals.forms.TutorialProposalForm",
    "talk": "djcon.proposals.forms.TalkProposalForm",
    "poster": "djcon.proposals.forms.PosterProposalForm",
}

THUMBNAIL_EXTENSION = "PNG"

ACCEPTING_PROPOSALS = True

SCHEDULE_TIMEZONE = "US/Eastern"

# local_settings.py can be used to override environment-specific settings
# like database and email that differ between development and production.
try:
    from local_settings import *
except ImportError:
    pass
