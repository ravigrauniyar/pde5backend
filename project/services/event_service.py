from datetime import datetime
from project.models.event import Event
from django.shortcuts import get_object_or_404

class EventService:
    def list(request):
        source_filter = request.query_params.get('source', None)
        start_datetime = request.GET.get('start_datetime')
        end_datetime = request.GET.get('end_datetime')
        
        queryset = Event.objects.all()
        
        if source_filter:
            queryset = queryset.filter(source__name__icontains=source_filter)

        if start_datetime:
            queryset = queryset.filter(properties__timestamp__gte=start_datetime)

        if end_datetime:
            queryset = queryset.filter(properties__timestamp__lte=end_datetime)
        return queryset
    
    def retrieve(id):
        return get_object_or_404(Event, id=id)
    
    # Adding event created timestamp in properties field
    def create(data):
        properties = data.pop('properties', {})
        current_datetime = datetime.now().replace(microsecond=0).isoformat()
        properties['timestamp'] = str(current_datetime)
        return Event.objects.create(**data, properties=properties)