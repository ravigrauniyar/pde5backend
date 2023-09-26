from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from project.services.project_service import ProjectService
from project.serializers.project_seriailzer import ProjectDetailSerializer, ProjectListSerializer, ProjectUpdateSerializer


class ProjectListView(APIView):
    def get(self, request):
        projects = ProjectService.list()
        seriailzer = ProjectListSerializer(projects, many=True)
        return Response(data=seriailzer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = ProjectDetailSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        project = ProjectService.create(data=serializer.validated_data)
        serializer = ProjectDetailSerializer(project)
        return Response(data=serializer.data, status=status.HTTP_201_CREATED)


class ProjectDetailView(APIView):
    def get(self, request, project_id):
        project = ProjectService.retrieve(id=project_id)
        serializer = ProjectDetailSerializer(project)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def put(self, request, id):
        project = ProjectService.retrieve(id)
        serializer = ProjectUpdateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        updated_project = ProjectService.update(project, serializer.data)
        serializer = ProjectDetailSerializer(updated_project)
        return Response(data=serializer.data, status=status.HTTP_200_OK)