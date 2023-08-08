from django.db import models

# Create your models here.

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    goal = models.IntegerField()
    image = models.URLField()
    is_open = models.BooleanField()
    date_created = models.DateTimeField()
    owner = models.CharField(max_length=200)

class Pledge(models.Model):
    amount = models.IntegerField()
    comment = models.CharField(max_length=200)
    anonymous = models.BooleanField()
    project = models.ForeignKey(  # each Pledge needs to have the ID of a Project saved in this field. 
        'Project',
        on_delete=models.CASCADE,  # if a Project gets deleted, we will also delete all of its pledges from the db.
        related_name='pledges' # when we supply a value for the "related_name" argument, Django automatically sets up a "property" on the Project model. It's like a field, but it doesn't have its own column in the db. So we can get all the pledges associated with a Project  (all_pledges = some_project.pledges)
    )
    supporter = models.CharField(max_length=200)