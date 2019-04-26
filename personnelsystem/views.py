from django.shortcuts import render
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

