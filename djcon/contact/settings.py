from django.conf import settings

use_captcha = getattr(settings, 'CONTACT_CAPTCHA', True)
use_honeypot = getattr(settings, 'CONTACT_HONEYPOT', True)
use_submitpath = getattr(settings, 'CONTACT_SUBMITPATH', False)
