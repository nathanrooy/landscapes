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