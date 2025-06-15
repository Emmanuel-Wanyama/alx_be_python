def safe_divide(numerator, denominator):
    """
    Performs division, handles potential errors.

    Args:
        numerator: The number to be divided.
        denominator: The number to divide by.

    Returns:
        A message for errors or the result for successful division.
    """
    try:
        num = float(numerator)
        den = float(denominator)
    except ValueError:
        return "Error: Please enter numeric values only."

    try:
        result = num / den
        return result
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."