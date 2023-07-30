import pytest


@pytest.mark.django_db
def test_create_ad(client, user, category, user_token):
    data = {
        'name': 'test ad text',
        'price': 2,
        'description': '',
        'is_published': False,
        'author': user.pk,
        'category': category.pk
    }

    expected_response = {
        'name': 'test ad text',
        'price': 2,
        'description': '',
        'is_published': False,
        'author': user.pk,
        'category': category.pk
    }

    response = client.post(
        '/ad/',
        data,
        format='json',
        HTTP_AUTHORIZATION=f'Bearer {user_token}',
    )
    response.data.pop('id')

    assert response.data == expected_response
    assert response.status_code == 201


@pytest.mark.django_db
def test_create_ad_name_too_short(client, user, category, user_token):
    data = {
        'name': 'test',
        'price': 2,
        'description': '',
        'is_published': False,
        'author': user.pk,
        'category': category.pk
    }

    expected_response = {
        'name': ['Ensure this field has at least 10 characters.']
    }

    response = client.post(
        '/ad/',
        data,
        format='json',
        HTTP_AUTHORIZATION=f'Bearer {user_token}',
    )

    assert response.data == expected_response
    assert response.status_code == 400


@pytest.mark.django_db
def test_create_ad_published(client, user, category, user_token):
    data = {
        'name': 'test ad text',
        'price': 2,
        'description': '',
        'is_published': True,
        'author': user.pk,
        'category': category.pk
    }

    expected_response = {
        'is_published': ['Value has to be False']
    }

    response = client.post(
        '/ad/',
        data,
        format='json',
        HTTP_AUTHORIZATION=f'Bearer {user_token}',
    )

    assert response.data == expected_response
    assert response.status_code == 400
