from django.dispatch import receiver
from django.db.models.signals import post_save
from project.models.source import Source


@receiver(post_save, sender='project.Project')
def create_default_source(sender, instance, created, **kwargs):
    if created:
        Source.objects.create(name='default', tag='default-source', project=instance)