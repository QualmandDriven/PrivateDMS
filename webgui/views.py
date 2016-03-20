from django.shortcuts import render
from django.http import HttpResponse

from django.views import generic

# Create your views here.
def index(request):
    return HttpResponse("Hi there")


class IndexView(generic.ListView):
    template_name = "webgui/index.html"

    def get_queryset(self):
        return
