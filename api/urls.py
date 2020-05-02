from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^get_sender/', views.get_sender),
    url(r'^echo/', views.echo)
]