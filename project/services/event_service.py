import datetime
from project.models.source import Source
from django.shortcuts import get_list_or_404, get_object_or_404
from project.models.event import Event
from django.db.models import Q

class EventService:
    def list(request):
        source_filters = request.GET.getlist('source')
        start_datetime = request.GET.get('start_datetime')
        end_datetime = request.GET.get('end_datetime')
        
        queryset = Event.objects.all()
        
        if source_filters:
            source_filter_q = Q()
            for source_filter in source_filters:
                source_filter_q |= Q(source__name__icontains=source_filter)
            
            queryset = queryset.filter(source_filter_q)

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