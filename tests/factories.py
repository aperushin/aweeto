import factory
from factory.fuzzy import FuzzyText

from ads.models import Ad, Category
from users.models import User, UserRoles, Location


class LocationFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Location

    name = 'test_location'
    lat = None
    lng = None


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Faker('name')
    password = '123qwe'
    email = factory.Faker('email')
    role = UserRoles.MEMBER
    birth_date = None

    @factory.post_generation
    def location(self, create, *args, **kwargs):
        if not create:
            # Simple build, or nothing to add, do nothing.
            return

        self.location.add(LocationFactory.create())


class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Category

    name = 'test_category'
    slug = FuzzyText(length=10)


class AdFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Ad

    name = 'test ad name'
    author = factory.SubFactory(UserFactory)
    price = 2
    description = 'test'
    is_published = False
    image = None
    category = factory.SubFactory(CategoryFactory)
