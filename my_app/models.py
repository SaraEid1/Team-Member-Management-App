from django.db import models


class TeamMember (models.Model):
    # id, info (firstname, lastname, email, phone number), role
    id = models.AutoField(primary_key=True) #unique id for each team member
    firstname = models.CharField (max_length=250)
    lastname = models.CharField (max_length=250)
    email = models.EmailField (max_length=250)
    phonenumber = models.CharField(max_length=12)
    role = models.CharField (max_length=100)
