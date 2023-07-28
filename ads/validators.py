from rest_framework import serializers


def is_false(value: bool) -> None:
    """
    Validator checking if a value is False
    """
    if value is not False:
        raise serializers.ValidationError('Value has to be False')
