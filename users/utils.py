from datetime import date


def calculate_age(birth_date: date):
    """
    Calculates age in years from a birthdate
    """
    today = date.today()
    return today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
