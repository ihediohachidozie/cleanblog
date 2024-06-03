from django.urls import path
from . import views

app_name = "cleanblog"

urlpatterns = [
    path("", views.HomeView.as_view(), name="home"),
    path("about/", views.AboutView.as_view(), name="about"),
    path("post/", views.PostView.as_view(), name="post"),
    path("contact/", views.ContactView.as_view(), name="contact"),
    path("sendmail/", views.sendmail, name="sendmail")
]
