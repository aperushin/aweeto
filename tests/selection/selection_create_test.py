import pytest


@pytest.mark.django_db
def test_create_selection(client, user, ad, user_token):
    data = {
        'name': 'test selection',
        'owner': user.id,
        'items': [ad.pk],
    }

    response = client.post(
        '/selection/',
        data,
        format='json',
        HTTP_AUTHORIZATION=f'Bearer {user_token}',
    )

    assert response.data.get('name') == data['name']
    assert response.data['items'] == data['items']
    assert response.data['owner'] != data['owner']  # Since the requesting user is set as the owner
    assert response.status_code == 201
