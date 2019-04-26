from django.forms import ModelForm
from . import models


"""
    The class below allows us to use a form to update our Personnel model
    Notice it uses ModelForm rather than forms.Form because this will update the table in our db
"""


class PersonnelForm(ModelForm):
    class Meta:
        model = models.Personnel
        fields = ['first_name', 'last_name', 'employee_number', 'academic_qualification']

