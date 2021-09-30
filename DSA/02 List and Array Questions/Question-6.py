""" Permutation of Words : If two words are permutation of each other that means they have same letters but in different order
ex. peek, keep """

def permutation(list1, list2):
    list2.reverse()
    if list1 == list2:
        return True
    return False

print(permutation(['p', 'e', 'e', 'k'], ['k', 'e', 'e', 'p']))



