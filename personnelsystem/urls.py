from django.urls import path
from .views import index, PersonnelListView, edit_personnel, delete_personnel

urlpatterns = [
    path('', index, name='index'),
    path('personnel-list/', PersonnelListView.as_view(), name='personnel-list'),
    path('<int:pk>/personnel-edit/', edit_personnel, name='personnel-edit'),
    path('<int:pk>/personnel-delete/', delete_personnel, name='personnel-delete'),
]

