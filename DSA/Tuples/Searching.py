animals = ('cow', 'ox', 'lion', 'monkey')

# using in operator
print('cow' in animals)

# Linear search
def searching(tup, element):
    for i in tup:
        if i == element:
            return tup.index(i)
    return "Element doesn't exist"

print(searching(animals, 'ox'))