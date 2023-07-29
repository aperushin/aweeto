from pytest_factoryboy import register

from tests.factories import AdFactory, UserFactory, LocationFactory, CategoryFactory

pytest_plugins = 'tests.fixtures'

register(AdFactory)
register(UserFactory)
register(LocationFactory)
register(CategoryFactory)
