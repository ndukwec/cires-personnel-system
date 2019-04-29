from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView
from personnelsystem.models import Personnel
from .forms import PersonnelForm


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


def edit_personnel(request, pk):
    # For debugging
    # personnel = get_object_or_404(Personnel, pk=pk)
    # from django.http import HttpResponse
    # return HttpResponse("Editing personnel with id: " + str(personnel.id))
    # For debugging

    # Code below do the actual work of updating the person and saving it to our db.
    personnel = get_object_or_404(Personnel, pk=pk)
    if request.method == "POST":
        form = PersonnelForm(request.POST, instance=personnel)
        if form.is_valid():
            personnel = form.save(commit=False)  # Commit is set to false to allow us to do more custom processing to
            # the personnel instance if we wish
            personnel.save()
            return redirect('personnel-list')
    else:
        form = PersonnelForm()
    return render(request, 'personnel-edit.html', {'form': form})


