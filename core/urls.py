from django.urls import path
from . import views

urlpatterns = [
    path("ping/", views.ping, name="ping"),
    path("api/waitlist/", views.waitlist_create, name="waitlist"),
]