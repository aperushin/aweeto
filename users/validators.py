from datetime import date
from django.core import exceptions
from django.utils.deconstruct import deconstructible

from users.utils import calculate_age


@deconstructible
class NotOnDomainValidator:
    """
    Check that an email does not end with any of specified domain names
    """
    def __init__(self, domain_list: str | list[str]):
        if not isinstance(domain_list, list):
            domain_list = [domain_list]

        self.domain_list = domain_list

    def __call__(self, value: str):
        value = value.rstrip('.').lower()
        for domain in self.domain_list:
            if value.endswith(domain):
                raise exceptions.ValidationError(f'Addresses on {domain} are not allowed')

    def __eq__(self, other):
        return self.domain_list == other.domain_list


@deconstructible
class IsOlderThanValidator:
    """
    Check that given birthdate corresponds to an age no less than specified
    """
    def __init__(self, minimum_age: int):
        self.minimum_age = minimum_age

    def __call__(self, birth_date: date):
        if calculate_age(birth_date) < self.minimum_age:
            raise exceptions.ValidationError(f'You have to be at least {self.minimum_age} years old')

    def __eq__(self, other):
        return self.minimum_age == other.minimum_age
