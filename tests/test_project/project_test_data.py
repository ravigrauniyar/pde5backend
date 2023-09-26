import factory
from project.models.project import Project

class ProjectFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Project

    title = factory.Faker('sentence', nb_words=3)
    description = factory.Faker('text', max_nb_chars=250)
    is_active = factory.Faker('boolean')