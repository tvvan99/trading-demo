def feq(actual: str, expected: str) -> bool:
    """Compare two numeric strings as floats to handle trailing decimal zeros.

    Example: feq("100.00000", "100") → True
    """
    return float(actual) == float(expected)
