from django import forms

class Html5DateInput(forms.DateInput):
    input_type = 'date'


class NewDmsDocumentForm(forms.Form):
    name = forms.CharField(max_length=100, label='Name')
    description = forms.CharField(widget=forms.Textarea, label='Description')
    filename = forms.FileField(label='Select a document')
    tags = forms.CharField(max_length=100, label='Tags')
    date = forms.DateField(widget=Html5DateInput, label='Date of document')


class DmsDocumentSearchForm(forms.Form):
    tags = forms.CharField(max_length=200, label='Tags')
