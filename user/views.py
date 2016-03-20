from django import template
from django.contrib.auth.models import User
from django.views import generic
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render_to_response

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from .models import DmsUser

from collections import defaultdict

register = template.Library()


class LoggedInMixin(object):

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(LoggedInMixin, self).dispatch(*args, **kwargs)


class ProfileView(LoggedInMixin, generic.DetailView):
    template_name = "user/profile.html"

    def get_object(self, queryset=None):
        return self.request.user


class LoginView(generic.ListView):
    template_name = "user/login.html"

    def get_queryset(self):
        return User.objects


def login_view(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)

    if user is not None:
        if user.is_active:
            login(request, user)
        #else:
            #Disabled
    #else:
        # invalid login

    return render_to_response(template_name="user/login.html")


