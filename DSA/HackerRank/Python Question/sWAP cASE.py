"""
You are given a string and your task is to swap cases. In other words, convert all lowercase letters to uppercase letters and vice versa.

For Example:

Www.HackerRank.com → wWW.hACKERrANK.COM
Pythonist 2 → pYTHONIST 2  
Function Description

Complete the swap_case function in the editor below.

swap_case has the following parameters:

string s: the string to modify
Returns

string: the modified string
Input Format

A single line containing a string s.

Constraints
0 < len(s) <= 1000

Sample Input 0

HackerRank.com presents "Pythonist 2".
Sample Output 0

hACKERrANK.COM PRESENTS "pYTHONIST 2".
"""

#Solution
def swap_case(s):
    uniList = []
    convList = []
    for i in s:
        uniList.append(i)
    for i in range(0, len(uniList)):
        if uniList[i].isupper() is True:
            convList.append(uniList[i].lower())
        else:
            convList.append(uniList[i].upper())
    convWord = ''.join(convList)
    return convWord

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)