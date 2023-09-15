from django.contrib import admin
from project.models.project import Project
from project.models.source import Source

admin.register(Project)
admin.register(Source)