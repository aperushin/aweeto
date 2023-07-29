import pytest


@pytest.mark.django_db
def test_create_selection_admin(client, user, ad, admin_token):
    data = {
        'name': 'test selection',
        'owner': user.id,
        'items': [ad.pk],
    }

    expected_response = {
        'id': 1,
        'name': 'test selection',
        'owner': user.id,
        'items': [ad.pk],
    }

    response = client.post(
        '/selection/',
        data,
        format='json',
        HTTP_AUTHORIZATION=f'Bearer {admin_token}',
    )

    assert response.data == expected_response
    assert response.status_code == 201


@pytest.mark.django_db
def test_create_selection_admin_ownerless(client, user, ad, admin_token_and_id):
    token, user_id = admin_token_and_id
    data = {
        'name': 'test selection',
        'items': [ad.pk],
    }

    expected_response = {
        'id': 2,
        'name': 'test selection',
        'owner': user_id,
        'items': [ad.pk],
    }

    response = client.post(
        '/selection/',
        data,
        format='json',
        HTTP_AUTHORIZATION=f'Bearer {token}',
    )

    assert response.data == expected_response
    assert response.status_code == 201


@pytest.mark.django_db
def test_create_selection_user(client, user, ad, user_token_and_id):
    token, user_id = user_token_and_id
    other_user_id = user.id

    data = {
        'name': 'test selection',
        'items': [ad.pk],
        'owner': other_user_id,
    }

    expected_response = {
        'id': 3,
        'name': 'test selection',
        'owner': user_id,
        'items': [ad.pk],
    }

    response = client.post(
        '/selection/',
        data,
        format='json',
        HTTP_AUTHORIZATION=f'Bearer {token}',
    )

    assert response.data == expected_response
    assert response.status_code == 201
