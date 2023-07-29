import pytest


@pytest.mark.django_db
def test_retrieve_ad(client, ad, user_token):
    expected_response = {
        'id': ad.pk,
        'name': ad.name,
        'author': ad.author_id,
        'price': ad.price,
        'description': ad.description,
        'is_published': False,
        'image': None,
        'category': ad.category_id
    }

    response = client.get(f'/ad/{ad.pk}/', HTTP_AUTHORIZATION=f'Bearer {user_token}')

    assert response.data == expected_response
    assert response.status_code == 200


@pytest.mark.django_db
def test_retrieve_ad_unauthorized(client, ad, user_token):
    expected_response = {
        "detail": "Authentication credentials were not provided."
    }

    response = client.get(f'/ad/{ad.pk}/')

    assert response.data == expected_response
    assert response.status_code == 401
