from django import forms
from django.core.mail import send_mail


class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
    email = forms.EmailField()
    cc_myself = forms.BooleanField(required=False)

    def sendmail(self):
        fullname = self.cleaned_data["name"]
        email = self.cleaned_data["email"]
        subject = self.cleaned_data["subject"]
        message = self.cleaned_data["message"] + "\nFrom:\n" + fullname
        recipients = ["ihediohachidozie@gmail.com"]

        send_mail(subject, message, email, recipients)
