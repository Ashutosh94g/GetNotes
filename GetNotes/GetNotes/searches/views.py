from django.shortcuts import render
from notes.models import Notes
from .models import SeachQuary

# Create your views here.
def search_view(request):
    query = request.GET.get('q', None)
    context = {'query': query}
    if query is not None:
        SeachQuary.objects.create(query=query)
        note_list = Notes.objects.search(query=query)
        context['note_list']=note_list
    return render(request, 'searches/views.html', context)
