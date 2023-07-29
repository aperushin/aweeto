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
        'id': 1,
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

    assert response.data == expected_response
    assert response.status_code == 201
