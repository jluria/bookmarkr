from django import forms
from bookmarks.models import List, Link
from django.forms.models import modelform_factory

ListForm = modelform_factory(List, fields=("name", "links"))

"""
class ListForm(forms.ModelForm):
    name = forms.CharField(max_length=50, help_text="Name Your List", required=True)
    links = forms.ChoiceField(choices=Link.objects.get(pk=1))

    class Meta:
        model = List
        fields = ['name', 'links']
"""
