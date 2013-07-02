import csv
import StringIO

from django import forms
from django.contrib import admin
from django.http import HttpResponse

from djcon.contact.models import Submission
from djcon.contact.settings import use_submitpath

CSV_HEADERS=['ID', 'Date', 'Name', 'Subject',
             'E-mail', 'Phone', 'Message']

class SubmissionAdmin(admin.ModelAdmin):
    list_display = ('contact_timestamp', 'contact_name', 'contact_email', 
        'contact_subject', 'contact_message')
    actions = ['export_csv']
    if not use_submitpath:
        exclude = ('contact_submit_path',)

    def export_csv(self, request, queryset):
        csv_data = StringIO.StringIO()
        csv_writer = csv.writer(csv_data)
        csv_writer.writerow(CSV_HEADERS)
        for contact in queryset:
            csv_writer.writerow([
                contact.id,
                contact.contact_timestamp,
                contact.contact_name,
                contact.contact_email,
                contact.contact_subject,
                contact.contact_phone,
                contact.contact_message
                ])
        csv_data.seek(0)
        response = HttpResponse(csv_data.read(), mimetype=u'text/csv')
        response['Content-Disposition'] = \
                                        u'attachment; filename=contactform.csv'
        return response

admin.site.register(Submission, SubmissionAdmin)
