from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from bookmarks.models import List, Link
from bookmarks.forms import ListForm

def index(request):
    all_lists = List.objects.all()

    return render(request, 'bookmarks/index.html', {'lists': all_lists})

def detail(request, list_id):
    l = List.objects.get(pk=list_id)
    all_links = l.links.all()

    return render(request, 'bookmarks/detail.html', {'list': l, 'links': all_links})

def create_list(request):
    if request.method == 'POST':
        form = ListForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print(form.errors)
    else:
        form = ListForm()

    return render(request, 'bookmarks/create_list.html', { 'form': form })
