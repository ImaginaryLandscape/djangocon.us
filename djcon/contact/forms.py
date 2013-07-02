from django import forms
from djcon.contact import models
from djcon.contact.settings import use_captcha, use_honeypot
from django.conf import settings

class ModelContactUsForm(forms.ModelForm):
    if use_captcha:
        from djcon.contact.fields import ReCaptchaField
        contact_captcha = ReCaptchaField()
    if use_honeypot:
        name2 = forms.CharField(required=False,
            widget=forms.TextInput(attrs={'style':'display:none;'}), label='')

        def clean_name2(self):
            """Check that nothing's been entered into the honeypot."""
            value = self.cleaned_data["name2"]
            if value:
                raise forms.ValidationError("Sorry, you appear to be spam")
            return value

    contact_submit_path = forms.CharField(required=False, label='',
        widget=forms.HiddenInput())
    is_contact = forms.CharField(required=False, label='',
        widget=forms.HiddenInput())

    class Meta:
        model = models.Submission
        exclude = ('contact_timestamp',)

