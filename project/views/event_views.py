from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

from project.models.source import Source
from project.services.event_service import EventService
from project.serializers.event_serializer import EventCreateSerializer, EventDetailSerializer, EventListSerializer

from drf_spectacular.utils import extend_schema

class EventListView(APIView):
    @extend_schema(
        request=EventListSerializer,
        responses=EventListSerializer
    )
    def get(self, request):
        events = EventService.list(request)
        if events.exists():
            serializer = EventListSerializer(events, many=True)
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_404_NOT_FOUND)


class EventDetailView(APIView):
    @extend_schema(
        request=EventListSerializer,
        responses=EventListSerializer
    )
    def get(self, request, id):
        event = EventService.retrieve(id)
        serializer = EventDetailSerializer(event)
        return Response(data=serializer.data, status=status.HTTP_200_OK)


class EventCreateView(APIView):
    authentication_classes = []
    permission_classes = [AllowAny]

    @extend_schema(
        request=EventListSerializer,
        responses=EventListSerializer
    )
    def post(self, request, key):
        api_key = request.META.get('HTTP_SOURCE_SECRET')
        source = Source.objects.filter(
            source_secret=api_key, source_key=key).first()
        if not source:
            return Response("Invalid Key or Secret", status=status.HTTP_406_NOT_ACCEPTABLE)

        serializer = EventCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.validated_data['source'] = source

        event = EventService.create(data=serializer.validated_data)
        serializer = EventDetailSerializer(event)

        return Response(data=serializer.data, status=status.HTTP_201_CREATED)
