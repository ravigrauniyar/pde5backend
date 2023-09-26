import uuid
import string
import secrets
from django.db import models
from project.models.project import Project

class Source(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField(null=True, blank=True)
    tag = models.CharField(max_length=100, blank=True, null=True)
    project = models.ForeignKey(Project, on_delete=models.DO_NOTHING)
    source_key = models.UUIDField(unique=True, default=uuid.uuid4)
    source_secret = models.CharField(max_length=40, unique=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)

    def generate_random_token(self, length=36):
        characters = string.ascii_letters + string.digits
        token = ''.join(secrets.choice(characters) for _ in range(length))
        return token

    def save(self, *args, **kwargs):
        self.source_secret = self.generate_random_token()
        return super(Source, self).save(*args, **kwargs)
