import uuid
import string
import factory
import secrets
from project.models.source import Source
from tests.test_project.project_test_data import ProjectFactory

class SourceFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Source

    name = factory.Faker('sentence', nb_words=3)
    description = factory.Faker('text', max_nb_chars=250)
    tag = factory.Faker('text', max_nb_chars=30)
    project = factory.SubFactory(ProjectFactory)
    @factory.lazy_attribute
    def source_key(self):
        return uuid.uuid4()

    @factory.lazy_attribute
    def source_secret(self):
        characters = string.ascii_letters + string.digits
        return ''.join(secrets.choice(characters) for _ in range(40))