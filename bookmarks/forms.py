from django import forms
from bookmarks.models import List, Link
from django.forms.models import modelform_factory

ListForm = modelform_factory(List, fields=("name", "links"))
