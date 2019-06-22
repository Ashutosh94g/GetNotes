"""from django.shortcuts import render, get_object_or_404"""
from django.shortcuts import render, get_object_or_404
from .models import Notes
from .forms import NotesModelForm
# Create your views here.
# CRUD -> Create Retrieve Update Delete

def notes_list_view(request):
    '''notes_list_view'''
    template_name = "notes/list.html"
    content = {'object_list': Notes.objects.all()}
    return render(request, template_name, content)


def notes_create_view(request):
    '''notes_create_view'''
    form = NotesModelForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = NotesModelForm(request.POST or None)
    template_name = "notes/form.html"
    content = {'form': form}
    return render(request, template_name, content)


def notes_retieve_view(request, slug):
    """notes_retieve_view"""
    notes_obj = get_object_or_404(Notes, slug=slug)
    template_name = "notes/retieve.html"
    content = {'object': notes_obj}
    return render(request, template_name, content)


def notes_update_view(request, slug):
    '''notes_update_view'''
    notes_obj = get_object_or_404(Notes, slug=slug)
    form = NotesModelForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = NotesModelForm(request.POST or None)
    template_name = "notes/form.html"
    content = {'object': notes_obj, 'form': form}
    return render(request, template_name, content)


def notes_delete_view(request, slug):
    """notes_delete_view"""
    notes_obj = get_object_or_404(Notes, slug=slug)
    template_name = "notes/delete.html"
    content = {'object': notes_obj, 'form': None}
    return render(request, template_name, content)
