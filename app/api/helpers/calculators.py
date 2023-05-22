from pendulum import date, now


def module_11(number: str, general: bool = False) -> int:
    """
    Module 11 - Bank Slip
    :param number: number to be calculated
    :param general: represents if the calculation is general DV or not
    :return: DV
    """
    number = number.replace(".", "").replace(" ", "")
    sum_ = 0
    maximum_number = 9

    for i, digit in enumerate(number[::-1]):
        pound_factor = i % 8
        multiplier = 2 + pound_factor
        sum_ += int(digit) * multiplier

    result = 11 - sum_ % 11

    if general and (result == 0 or result > maximum_number):
        return 1

    return 0 if result > maximum_number else result


def module_10(number: str) -> int:
    """Module 10 - Bank Slip"""
    number = number.replace(".", "").replace(" ", "")
    sum_ = 0
    maximum_number = 9
    for i, digit in enumerate(number[::-1]):
        pound_factor = i % 2
        multiplication = int(digit) * (2 - pound_factor)
        sum_ += sum(map(int, str(multiplication).strip())) if multiplication > maximum_number else multiplication
    result = 10 - sum_ % 10

    return 0 if result > maximum_number else result


def due_date_from_factor(factor: str) -> str:
    """Due date from factor"""
    atual_date = now().date()
    base_data = date(1997, 10, 7) if atual_date <= date(2025, 2, 22) else date(2025, 2, 22)

    return base_data.add(days=int(factor)).format("DD/MM/YYYY")
