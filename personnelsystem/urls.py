from django.urls import path
from .views import index, PersonnelListView

urlpatterns = [
    path('', index, name='index'),
    path('personnel-list/', PersonnelListView.as_view(), name='personnel-list'),
]

