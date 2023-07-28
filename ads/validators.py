from rest_framework import serializers


def is_false(value: bool) -> serializers.ValidationError | None:
    """
    Validator checking if a value is False
    """
    if value is not False:
        return serializers.ValidationError('Value has to be False')
