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