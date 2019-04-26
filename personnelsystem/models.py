from django.db import models


"""
    Below is a model representing employees/personnel in our system, this model will build our table in our db
    each property/field will represent a column in our table
"""


class Personnel(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    employee_number = models.IntegerField(unique=True)
    academic_qualification = models.CharField(max_length=50)


