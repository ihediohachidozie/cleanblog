from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.core.mail import send_mail


class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, help_text="Must be filled")
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
    email = forms.EmailField()
    cc_myself = forms.BooleanField(required=False)

    def sendmail(self):

        fullname = self.cleaned_data["name"]
        email = self.cleaned_data["email"]
        subject = self.cleaned_data["subject"]
        message = self.cleaned_data["message"] + "\nFrom:\n" + fullname + "\nEmail:\n" + email
        recipients = ["ihediohachidozie@gmail.com"]

        if not fullname:
            raise ValidationError(_('Invalid date - renewal in past'))

        send_mail(subject, message, email, recipients)
