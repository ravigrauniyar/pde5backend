from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from project.services.source_services import SourceService
from project.serializers.source_serializer import SourceListSerializer, SourceDetailSerializer

class SourceListView(APIView):
    def get(self, request):
        sources = SourceService.list()
        serializer = SourceListSerializer(sources, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = SourceListSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        source = SourceService.create(data=serializer.validated_data)
        serializer = SourceListSerializer(source)
        return Response(data=serializer.data, status=status.HTTP_201_CREATED)

class SourceDetailView(APIView):
    def get(self, request, id):
        source = SourceService.retrieve(id)
        serializer = SourceDetailSerializer(source)
        return Response(data=serializer.data, status=status.HTTP_200_OK)