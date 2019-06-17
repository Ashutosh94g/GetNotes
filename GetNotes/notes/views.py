from django.shortcuts import render , get_object_or_404
from .models import Notes
from .forms import NotesModelForm
# Create your views here.
# CRUD -> Create Retrieve Update Delete

def notes_list_view(request):
    qs = Notes.objects.all()
    template_name = "notes/list.html"
    content = {'object_list': qs}
    return render(request,template_name,content)


def notes_create_view(request):
    form = NotesModelForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = NotesModelForm(request.POST or None)
    template_name = "notes/create.html"
    content = {'form': form}
    return render(request,template_name,content)


def notes_retieve_view(request,slug):
    notes_obj = get_object_or_404(Notes,slug = slug)
    template_name = "notes/retieve.html"
    content = {'object': notes_obj}
    return render(request,template_name,content)


def notes_update_view(request):
    notes_obj = get_object_or_404(Notes,slug = slug)
    template_name = "notes/update.html"
    content = {'object': notes_obj,'form': None}
    return render(request,template_name,content)


def notes_delete_view(request):
    notes_obj = get_object_or_404(Notes,slug = slug)
    template_name = "notes/delete.html"
    content = {'object': notes_obj,'form': None}
    return render(request,template_name,content)
