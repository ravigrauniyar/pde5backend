import factory
from account.models import UserAccount

class EmailSignupFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = UserAccount

    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')
    email = factory.LazyAttribute(lambda obj: f'{obj.first_name.lower()}@test.com')
    password = factory.LazyAttribute(lambda obj: f'{obj.first_name}{obj.last_name}')