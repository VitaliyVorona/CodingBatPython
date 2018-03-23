def pos_neg(a, b, negative):
    if (a < 0 and b < 0) and negative:
        return True
    if (a < 0 and b < 0) and not negative:
        return False
    if (a < 0 or b < 0) and negative:
        return False
    if (a < 0 or b < 0) and not negative:
        return True
    return False
