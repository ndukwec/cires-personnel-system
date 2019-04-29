from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from personnelsystem.models import Personnel


def index(request):
    return render(request, 'index.html', {'context': 'homepage'})


"""
    class below will return a list view of all personnel in our db
"""


class PersonnelListView(ListView):
    template_name = 'personnel-list.html'
    queryset = Personnel.objects.all()
    context_object_name = 'personnel'
    paginate_by = 10
    ordering = ['last_name']


"""
    views below will handle the editing and deletion of a personnel object via its primary key
"""


def edit_personnel(request, pk=1):
    personnel = get_object_or_404(Personnel, pk=pk)
    from django.http import HttpResponse
    return HttpResponse("Editing personnel with id: " + str(personnel.id))


def delete_personnel(request, pk=1):
    personnel = get_object_or_404(Personnel, pk=pk)
    from django.http import HttpResponse
    return HttpResponse("Deleting personnel with id: " + str(personnel.id))

