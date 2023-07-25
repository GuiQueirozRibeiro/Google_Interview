'''
01.01 Is Unique: Implement an algorithm to determine if a string has all unique characters.
    What if you cannot use additional data structure.
'''

# Time: O(n) Space: O(n)

def uniqueCharacters(str):
    array = set()
    for i in str:
        if i in array:
            return False
        array.add(i)
    return True