def safe_division(n: float, d: float) -> float:
    '''Safe Division

    Parameters
    ----------
    n : float (numerator)
    d : float (denominator)

    Returns
    -------
    float

    Notes
    -----
    Specifically for handling the case when the denominator is 0.
    '''

    try:
        return n / d
    except ZeroDivisionError:
        return 0.0


