from project.models.source import Source
from django.shortcuts import get_object_or_404, get_list_or_404

class SourceService:
    def list(project_id):
        sources = Source.objects.filter(project_id=project_id)
        if sources:
            return sources
        return None
    
    def create(data, project_id):
        return Source.objects.create(**data, project_id=project_id)
    
    def retrieve(project_id, source_id):
        return get_object_or_404(Source, id=source_id, project_id=project_id)
    
    def update(instance, data):
        for key, value in data.items():
            setattr(instance, key, value)
        instance.save()
        return instance
    
    def delete(instance):
        return instance.delete()