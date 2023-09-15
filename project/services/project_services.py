from project.models.project import Project
from django.shortcuts import get_object_or_404, get_list_or_404

class ProjectService:
    def list():
        return get_list_or_404(Project)

    def create(data):
        return Project.objects.create(**data)
    
    def retrieve(id):
        return get_object_or_404(Project, id=id)

    def update(instance, data):
        for key, value in data.items():
            setattr(instance, key, value)
        instance.save()
        return instance