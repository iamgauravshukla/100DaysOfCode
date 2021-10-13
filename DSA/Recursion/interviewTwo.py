# power of any number
def power(base, exponent):
    assert exponent >= 0 and int(exponent) == exponent, 'Must be Positive and Integer number'
    if exponent == 0:
        return 1
    elif exponent == 1:
        return base
    else:
        return base * power(base, exponent - 1)


print(power(3, 2))
