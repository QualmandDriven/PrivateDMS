from django.conf.urls import url
from django.contrib.auth.views import login, logout
from . import views

"""url(r'^profile/(?P<pk>[0-9]+)/(?P<username>[a-z0-9]+)/$', views.ProfileView.as_view(), name='profile'),"""

urlpatterns = [
    url(r'^login/$',  login, name='login'),
    url(r'^logout/$',  logout, name='logout'),
    url(r'^profile/$', views.ProfileView.as_view(), name='profile'),
]