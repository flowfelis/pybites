def convert(value: float, fmt: str) -> float:
    """Converts the value to the designated format.

    :param value: The value to be converted must be numeric or raise a TypeError
    :param fmt: String indicating format to convert to
    :return: Float rounded to 4 decimal places after conversion
    """
    # input_argument = 79, expected_output = 31.1024
    fmt = fmt.lower()
    if not isinstance(value, float) and not isinstance(value, int):
        raise TypeError
    if fmt not in ('cm', 'in'):
        raise ValueError

    DECIMAL_PLACE = 4

    if fmt == 'cm':
        return round(value * 2.54, DECIMAL_PLACE)

    return round(value * 0.393700787, DECIMAL_PLACE)
