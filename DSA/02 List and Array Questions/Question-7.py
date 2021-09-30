# Palindrome  Words ex. level
def Palindrome(word):
    wordList = []
    revLi = []
    for i in word:
        wordList.append(i)
        revLi.append(i)
    revLi.reverse()
    if wordList == revLi:
        return "Given word is palindrome"

    return 'Given word is not palindrome'

print(Palindrome('level'))
