from rest_framework import serializers
from django.apps import apps

class PledgeSerializer(serializers.ModelSerializer): #ModelSerializer is a class provided by DRF, it's smart enough to inspect our model and figure out for itself how each field should be converted to JSON. We give our PledgeSerializer Class some "meta-info": what model should it serialize, and which fieldsmshould it include.
    supporter = serializers.ReadOnlyField(source='supporter.id')
    
    class Meta:
        model = apps.get_model('projects.Pledge')
        fields = '__all__'


class PledgeDetailSerializer(PledgeSerializer):

    def update(self, instance, validated_data): # we are telling the serializer how to perform an update on an existring instance of a Project. When it performs an update, it will get some validated data.
        instance.amount = validated_data.get('amount', instance.amount) # the serializer should go through each field on the instance, and try to get the new value from the validated_data. If it can't find a value in the validated_data, it can use the value that is already on the instance.
        instance.comment = validated_data.get('comment',instance.comment)
        instance.anonymous = validated_data.get('anonymous', instance.anonymous)
        instance.project = validated_data.get('project', instance.project)
        instance.supporter = validated_data.get('supporter', instance.supporter)
        instance.save()
        return instance


class ProjectSerializer(serializers.ModelSerializer):  # we splitted rojectSerializer in two: regular version and a detailed version, so that we can choose when we want to display the extra info.
    owner = serializers.ReadOnlyField(source='owner.id') # We are giving the serializer custom instructions for how it should handle the ownerfield on the Project model. We are saying that this field should be read-only. That means that users aren'tallowed to choose what value they set - our code is going to decide. Finally, we are saying that when the serializer gets handed data, it should find the owner in that data, grab the id field from that User object, and save that valuein the owner field. 
    
    class Meta:
        model = apps.get_model('projects.Project')
        fields ='__all__'

class ProjectDetailSerializer(ProjectSerializer):
    pledges = PledgeSerializer(many=True, read_only=True)  # we specified related_name = pledges in the Pledges model, which means that it acts as an additional field in Project model. This way we can add a depiction of a list of pledges associated with each Project to that project JSON. This is called "inheritance".We define the regular ProjectSerializer first. Thenwe say, basically, "oh, and we also have a ProjectDetailSerializer - it is the same asthe ProjectSerializer, except it has a list of pledges too!"

    def update(self, instance, validated_data): # we are telling the serializer how to perform an update on an existring instance of a Project. When it performs an update, it will get some validated data.
        instance.title = validated_data.get('title', instance.title) # the serializer should go through each field on the instance, and try to get the new value from the validated_data. If it can't find a value in the validated_data, it can use the value that is already on the instance.
        instance.description = validated_data.get('description',instance.description)
        instance.goal = validated_data.get('goal', instance.goal)
        instance.image = validated_data.get('image', instance.image)
        instance.is_open = validated_data.get('is_open', instance.is_open)
        instance.date_created = validated_data.get('date_created',instance.date_created)
        instance.owner = validated_data.get('owner', instance.owner)
        instance.save()
        return instance