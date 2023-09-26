from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from project.services.source_service import SourceService
from project.services.project_service import ProjectService
from project.serializers.source_serializer import SourceListSerializer, SourceDetailSerializer, SourceCreateSerializer, SourceUpdateSerializer

class SourceListView(APIView):
    def get(self, request, project_id):
        ProjectService.retrieve(id=project_id)
        sources = SourceService.list(project_id=project_id)
        if sources:
            serializer = SourceListSerializer(sources, many=True)
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        return Response("No content", status=status.HTTP_204_NO_CONTENT)
    
    def post(self, request, project_id):
        ProjectService.retrieve(id=project_id)
        serializer = SourceCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        source = SourceService.create(data=serializer.validated_data, project_id=project_id)
        serializer = SourceListSerializer(source)
        return Response(data=serializer.data, status=status.HTTP_201_CREATED)

class SourceDetailView(APIView):
    def get(self, request, project_id, source_id):
        ProjectService.retrieve(id=project_id)
        source = SourceService.retrieve(source_id=source_id)
        serializer = SourceDetailSerializer(source)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request, project_id, source_id):
        ProjectService.retrieve(id=project_id)
        source = SourceService.retrieve(source_id=source_id)
        serializer = SourceUpdateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        updated_source = SourceService.update(source, serializer.data)
        serializer = SourceDetailSerializer(updated_source)
        return Response(data=serializer.data, status=status.HTTP_202_ACCEPTED)
    
    def delete(self, request, project_id, source_id):
        ProjectService.retrieve(id=project_id)
        source = SourceService.retrieve(source_id=source_id)
        SourceService.delete(source)
        return Response("Source Deletes", status=status.HTTP_204_NO_CONTENT)