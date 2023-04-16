from django.contrib.auth.models import User
from django.db import models

class User_Data(models.Model):
    """Extending users to have types"""
    ADMINISTRATION = 1
    INSTRUCTOR = 2
    STUDENT = 3

    USERS = (
        (ADMINISTRATION,'Administration'),
        (INSTRUCTOR, 'Instructor'),
        (STUDENT, 'Student')
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_type = models.PositiveSmallIntegerField(choices=USERS, blank=True, null = True)
    
    