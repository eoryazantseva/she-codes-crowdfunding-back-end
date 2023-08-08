from rest_framework import serializers
from django.apps import apps

class PledgeSerializer(serializers.ModelSerializer): #ModelSerializer is a class provided by DRF, it's smart enough to inspect our model and figure out for itself how each field should be converted to JSON. We give our PledgeSerializer Class some "meta-info": what model should it serialize, and which fieldsmshould it include.
    class Meta:
        model = apps.get_model('projects.Pledge')
        fields = '__all__'



class ProjectSerializer(serializers.ModelSerializer):  # we splitted rojectSerializer in two: regular version and a detailed version, so that we can choose when we want to display the extra info.
    
    class Meta:
        model = apps.get_model('projects.Project')
        fields ='__all__'

class ProjectDetailSerializer(ProjectSerializer):
    pledges = PledgeSerializer(many=True, read_only=True)  # we specified related_name = pledges in the Pledges model, which means that it acts as an additional field in Project model. This way we can add a depiction of a list of pledges associated with each Project to that project JSON. This is called "inheritance".We define the regular ProjectSerializer first. Thenwe say, basically, "oh, and we also have a ProjectDetailSerializer - it is the same asthe ProjectSerializer, except it has a list of pledges too!"