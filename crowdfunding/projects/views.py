from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Project, Pledge
from .serializers import ProjectSerializer, PledgeSerializer, ProjectDetailSerializer
from django.http import Http404
from rest_framework import status


class ProjectList(APIView):

    def get(self, request):   # we're defining the behaviour this view should enact when it receives an HTTP request of the GET variety
        projects = Project.objects.all()    # this view retrieves a list of all projects from our db,
        serializer = ProjectSerializer(projects, many=True)  # serializes them into JSON, and 
        return Response(serializer.data) # sends that data back through the endpoint to the frontend.
    
    def post(self, request):  # if a POST request comes through,
        serializer = ProjectSerializer(data=request.data) # ... it should load the data into serializer,...
        if serializer.is_valid():
            serializer.save(owner=request.user) # ...tell the serializer to save a new record to the DB,...
            return Response(  # ...respond with the JSON detailing what was saved and a status code 201 (successfully created)
                serializer.data,
                status=status.HTTP_201_CREATED
            )
        return Response( #if our serialized data is not valid, we are returning a 400 code (bad request)
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )


class ProjectDetail(APIView):

    def get_object(self, pk): # when this view gets called, the front end will be asking for info about a specific project. This method says when the view goes looking for a project, it should use the promary key of that project. The view should grab the project with the pk from the db.
        try: # added try/except block to our get_object method. It tells Python to attempt to retrieve the record from the db. Bit, if it encounters a problem in the process, it raises an HTTP404 error (404 code to the front end)
            return Project.objects.get(pk=pk)
        except Project.DoesNotExist:
            raise Http404
        

    def get(self, request, pk): # also tells our our view how to handle GET requsests. This method says that the way to do this is to:
        project = self.get_object(pk) #  get the data from the db
        serializer = ProjectDetailSerializer(project) # serialize the data to JSON
        return Response(serializer.data) # return it as a response
    


class PledgeList(APIView):

    def get(self, request):
        pledges = Pledge.objects.all()
        serializer = PledgeSerializer(pledges, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PledgeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(supporter=request.user)
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )