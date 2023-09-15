from collections.abc import Iterable
import secrets
import string
from django.db import models
from project.models.project import Project

class Source(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField(null=True, blank=True)
    tag = models.CharField(max_length=100)
    project = models.ForeignKey(Project, on_delete=models.DO_NOTHING)
    token = models.CharField(max_length=150, unique=True)

    def generate_random_token(self, length=50):
        characters = string.ascii_letters + string.digits
        token = ''.join(secrets.choice(characters) for _ in range(length))
        return token

    def save(self, *args, **kwargs):
        self.token = self.generate_random_token()
        return super(Source, self).save(*args, **kwargs)
