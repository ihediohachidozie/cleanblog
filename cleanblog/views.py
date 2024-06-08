from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.contrib import messages
from .forms import ContactForm


class HomeView(generic.TemplateView):
    template_name = "cleanblog/index.html"


class AboutView(generic.TemplateView):
    template_name = "cleanblog/about.html"


class PostView(generic.TemplateView):
    template_name = "cleanblog/post.html"


class ContactView(generic.TemplateView):
    template_name = "cleanblog/contact.html"


def sendmail(request):
    if request.method == "POST":
        form = ContactForm(request.POST)

        if form.is_valid():
            form.sendmail()
            messages.success(request, f'Thank you. Your message is sent!')
            return HttpResponseRedirect(reverse('cleanblog:contact'))
        else:
            # modify to send back the form with the error message..
            # return HttpResponse('bad content')
            form = ContactForm()
            return render(request, 'cleanblog/contact.html', {'form': form})
