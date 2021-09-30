animals = {'wild': 'Lion', 'pet': 'Dog', 'birds': 'sparrow', 'carnivorous': 'Tiger'}

copiedDict = animals.copy()  # creates copy of dictionary
print(copiedDict)

# animals.clear()  # clears entire dictionary

# fromkeys method : it takes two perimeter syntax = dictionary.fromkeys(sequence[], values), values are optional
newDict = {}.fromkeys([1,2,3], 'a' )
print(newDict)

# get method syntax = dictionary.get(key, value = to be returned if key not found)
searched = animals.get('wild', 'Not found')
print(searched)

# items
print(animals.items())  # returns all (key, values) from dictionary

# keys(): returns the list of all the keys
print(animals.keys())

# setdefault(): syntax = dict.setdefault(key, value = to be assigned to that key if not found)
animals.setdefault('herbivorous', 'horse')
print(animals)

# values(): returns the list of all values of dictionary
print(animals.values())

# update()
petAnimal = {'bird': 'parrot', 'animal': 'dog'}
animals.update(petAnimal)
print(animals)
