from rest_framework import serializers
from django.apps import apps

class ProjectSerializer(serializers.ModelSerializer):  #ModelSerializer is a class provided by DRF, it's smart enough to inspect our model and figure out for itself how each field should be converted to JSON. We give our ProjectSerializer Class some "meta-info": what model should it serialize, and which fieldsmshould it include?
    class Meta:
        model = apps.get_model('projects.Project')
        fields ='__all__'

