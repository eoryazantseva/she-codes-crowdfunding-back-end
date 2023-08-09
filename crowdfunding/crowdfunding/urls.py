"""
URL configuration for crowdfunding project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('projects.urls')),
    path('', include('users.urls')),
    path('api-auth/', include('rest_framework.urls')), # URL for our log-in view, DRF supplies it for us. All we have to do is plug it into a URL.+ from .models import CustomUser+ from .serializers import CustomUserSerializer+ class CustomUserList(APIView):+   def get(self, request):+       users = CustomUser.objects.all()+       serializer = CustomUserSerializer(users, many=True)+       return Response(serializer.data)+   def post(self, request):+       serializer = CustomUserSerializer(data=request.data)+       if serializer.is_valid():+           serializer.save()+           return Response(serializer.data)+       return Response(serializer.errors)+ class CustomUserDetail(APIView):+   def get_object(self, pk):+       try:+           return CustomUser.objects.get(pk=pk)+       except CustomUser.DoesNotExist:+           raise Http404+   def get(self, request, pk):+       user = self.get_object(pk)+       serializer = CustomUserSerializer(user)+       return Response(serializer.data)from django.urls import pathfrom . import viewsurlpatterns = [    path('users/', views.CustomUserList.as_view()),    path('users/<int:pk>/', views.CustomUserDetail.as_view()),]

]
