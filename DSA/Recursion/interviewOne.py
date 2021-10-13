# Sum of digits of a number
def sumOfDigits(n):
    assert n >= 0 and int(n)==n, 'Positive and Integers Only'
    if n in [0, 1]:
        return n
    else:
        return int(n % 10) + sumOfDigits(int(n / 10))

print(sumOfDigits(121))
