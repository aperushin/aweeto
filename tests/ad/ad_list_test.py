import pytest

from ads.serializers import AdListSerializer
from tests.factories import AdFactory


@pytest.mark.django_db
def test_ad_list(client):
    ads_count = 10
    ads = AdFactory.create_batch(ads_count)

    expected_response = {
        'count': ads_count,
        'next': None,
        'previous': None,
        'results': AdListSerializer(ads, many=True).data
    }

    response = client.get('/ad/')

    assert response.data == expected_response
    assert response.status_code == 200
