import pytest

from users.models import UserRoles


@pytest.fixture
@pytest.mark.django_db
def user_token(client, django_user_model):
    username = 'test_user'
    password = '123qwe'

    django_user_model.objects.create_user(
        username=username,
        password=password,
        role=UserRoles.MEMBER,
        email='user@test.com',
    )

    response = client.post(
        '/token/',
        {'username': username, 'password': password},
        format='json',
    )

    return response.data['access']


@pytest.fixture
@pytest.mark.django_db
def admin_token(client, django_user_model):
    username = 'test_admin'
    password = '123qwe'

    django_user_model.objects.create_user(
        username=username,
        password=password,
        role=UserRoles.ADMIN,
        email='admin@test.com',
    )

    response = client.post(
        '/token/',
        {'username': username, 'password': password},
        format='json',
    )

    return response.data['access']


@pytest.fixture
@pytest.mark.django_db
def user_token_and_id(client, django_user_model):
    username = 'test_user_2'
    password = '123qwe'

    user = django_user_model.objects.create_user(
        username=username,
        password=password,
        role=UserRoles.MEMBER,
        email='user2@test.com',
    )

    response = client.post(
        '/token/',
        {'username': username, 'password': password},
        format='json',
    )

    return response.data['access'], user.id


@pytest.fixture
@pytest.mark.django_db
def admin_token_and_id(client, django_user_model):
    username = 'test_admin_2'
    password = '123qwe'

    user = django_user_model.objects.create_user(
        username=username,
        password=password,
        role=UserRoles.ADMIN,
        email='admin2@test.com',
    )

    response = client.post(
        '/token/',
        {'username': username, 'password': password},
        format='json',
    )

    return response.data['access'], user.id
