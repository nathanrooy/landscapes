def safe_division(n,d):
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

    try: return n/d
    except ZeroDivisionError: return 0


def prod(x):
    '''Product (replaces math.prod)

    Parameters
    ----------
    x : list

    Returns 
    -------
    float

    Notes
    -----
    keeping this here for backwards compatibility since math.prod was 
    introduced in py3.8
    '''

    total = 1
    for v in x: total *= v 
    return total