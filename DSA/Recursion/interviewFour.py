def decTobin(n):
    assert n == int(n), 'Only integers value'
    if n == 0:
        return 0
    else:
        return n % 2 + 10 * decTobin(int(n/2))


print(decTobin(1.3))