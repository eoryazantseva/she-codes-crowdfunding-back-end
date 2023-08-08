from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Project
from .serializers import ProjectSerializer

class ProjectList(APIView):

    def get(self, request):   # we're defining the behaviour this view should enact when it receives an HTTP request of the GET variety
        projects = Project.objects.all()    # this view retrieves a list of all projects from our db,
        serializer = ProjectSerializer(projects, many=True)  # serializes them into JSON, and 
        return Response(serializer.data) # sends that data back through the endpoint to the frontend.
    
    def post(self, request):  # if a POST request comes through,
        serializer = ProjectSerializer(data=request.data) # ... it should load the data into serializer,...
        if serializer.is_valid():
            serializer.save() # ...tell the serializer to save a new record to the DB,...
            return Response(serializer.data) # ...respond with the JSON detailing what was saved
        

class ProjectDetail(APIView):

    def get_object(self, pk): # when this view gets called, the front end will be asking for info about a specific project. This method says when the view goes looking for a project, it should use the promary key of that project. 
        return Project.objects.get(pk=pk) # The view should grab the project with the pk from the db.
    
    def get(self, request, pk): # also tells our our view how to handle GET requsests. This method says that the way to do this is to:
        project = self.get_object(pk) #  get the data from the db
        serializer = ProjectSerializer(project) # serialize the data to JSON
        return Response(serializer.data) # return it as a response