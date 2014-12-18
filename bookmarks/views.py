from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
from bookmarks.models import List

def index(request):
    all_lists = List.objects.all()

    return render(request, 'bookmarks/index.html', {'lists': all_lists})

def detail(request, list_id):
    l = List.objects.get(pk=list_id)
    all_links = l.links.all()

    return render(request, 'bookmarks/detail.html', {'list': l, 'links': all_links})
