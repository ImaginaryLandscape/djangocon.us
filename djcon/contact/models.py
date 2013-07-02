from django.db import models
from datetime import datetime

class Submission(models.Model):
    contact_email = models.EmailField('Email')
    contact_name = models.CharField('Name', max_length=200, blank=True)
    contact_subject = models.CharField ('Subject', max_length=200, blank=True)
    contact_phone = models.CharField ('Telephone', max_length=20, blank=True)
    contact_message = models.TextField ('Comments', blank=True)
    contact_submit_path = models.CharField (max_length=300, blank=True)
    contact_timestamp = models.DateTimeField(default=datetime.now, blank=True)
