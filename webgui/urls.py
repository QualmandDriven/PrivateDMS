from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^$', views.get_documents),
    url(r'^newdocument$', views.get_new_document),
]