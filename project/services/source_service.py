from project.models.source import Source
from django.shortcuts import get_object_or_404, get_list_or_404

class SourceService:
    def list():
        return get_list_or_404(Source)
    
    def create(data):
        return Source.objects.create(**data)
    
    def retrieve(id):
        return get_object_or_404(Source, id=id)