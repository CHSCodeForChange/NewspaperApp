from django.db import models
from django.contrib.auth.models import User
from django.db.models import Q


# Create your models here.

class Paper(models.Model):
    owner = models.ForeignKey(
        User,
        models.CASCADE,
        null=True
    )

    name = models.CharField(max_length=60, null=False, blank=False)
    school = models.CharField(max_length=60, null=False, blank=False)
    description = models.CharField(max_length=400, null=False, blank=False)
    city = models.CharField(max_length=60, null=False, blank=False)
    state = models.CharField(max_length=30, null=False, blank=False)

    #this is especially important as it is needed to get the JSON data
    website = models.URLField(null=False, blank=False)

    #this is how readers will connect the app to their paper, similar to a Kahoot! code
    code = models.IntegerField(blank=True, null=True)

    def get_users_list(user):
        return Paper.objects.filter(owner=user)




class Section(models.Model):
    parentPaper = models.ForeignKey(
        Paper,
        on_delete=models.CASCADE,
        null=False,
    )

    #this is the actual name of the section
    name = models.CharField(max_length=120, null=False, blank=False)

    #this is the category tag that is registered in wordpress
    wordpressTag = models.CharField(max_length=120, null=False, blank=False)
