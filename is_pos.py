def is_positive_float(n):
    try:
        float_n = float(n)
        if float_n > 0:
            valid = True
        else:
            valid = False
    except ValueError:
        valid = False
    return valid