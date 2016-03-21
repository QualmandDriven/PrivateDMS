from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from django.utils import timezone

from .forms import NewDmsDocumentForm, DmsDocumentSearchForm

from dmsmodel import models


class FormListView(generic.edit.FormMixin, generic.ListView):
    def get(self, request, *args, **kwargs):
        # From ProcessFormMixin
        form_class = self.get_form_class()
        self.form = self.get_form(form_class)

        # From BaseListView
        self.object_list = self.get_queryset()
        allow_empty = self.get_allow_empty()
        if not allow_empty and len(self.object_list) == 0:
            raise Http404(_(u"Empty list and '%(class_name)s.allow_empty' is False.")
                          % {'class_name': self.__class__.__name__})

        context = self.get_context_data(object_list=self.object_list, form=self.form)
        return self.render_to_response(context)

    def post(self, request, *args, **kwargs):
        return self.get(request, *args, **kwargs)


class DmsDocumentsView(FormListView):
    template_name = "webgui/index.html"
    form_class = DmsDocumentSearchForm
    model = models.DmsDocument.objects.all().order_by('-uploaded')


class IndexView(generic.ListView):
    template_name = "webgui/index.html"

    def get_queryset(self):
        return models.DmsDocument.objects.all().order_by('-uploaded')

    def post(self, request):
        my_form = DmsDocumentSearchForm(request.POST)
        if my_form.is_valid():
            tag = my_form.cleaned_data['tags']
            context['all_documents_list'] = models.DmsDocument.objects.filter(tags__name=tag)

        return render(request, "webgui/index.html", context)


def get_documents(request):
    object_list = models.DmsDocument.objects.all().order_by('-uploaded')
    if request.method == 'POST':
        form = DmsDocumentSearchForm(request.POST)

        if form.is_valid():
            tagsstring = form.cleaned_data['tags']
            tags = tagsstring.split(',')
            for tag in tags:
                tag = tag.strip()
            object_list = models.DmsDocument.objects.filter(tags__name__in=tags)
    else:
        form = DmsDocumentSearchForm()

    return render(request, 'webgui/index.html', {'form': form, 'object_list': object_list})


def get_new_document(request):
    if request.method == 'POST':
        form = NewDmsDocumentForm(request.POST, request.FILES)

        if form.is_valid():
            newDocument = models.DmsDocument()
            newDocument.name = form.cleaned_data['name']
            newDocument.date = form.cleaned_data['date']
            newDocument.uploaded = timezone.now()
            newDocument.filename = request.FILES['filename']
            newDocument.description = form.cleaned_data['description']
            newDocument.save()
            newDocument.add_tags(tags=form.cleaned_data['tags'].split(','))

            return HttpResponseRedirect('/')

    else:
        form = NewDmsDocumentForm()

    return render(request, 'webgui/new_document.html', {'form': form})
