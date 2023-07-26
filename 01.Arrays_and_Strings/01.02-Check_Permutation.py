'''
01.02 Check Permutation: Given two strings, write a method to decide if one is a permutation of the
    other.
'''

# Time: O(n) Space: O(n)
def is_permutation(a, b):
    if len(a) != len(b):
        return False
    count = [0] * 256
    for i in a: # O(n)
        count[ord(i)] += 1
    for i in b: # O(n)
        count[ord(i)] -= 1        
    for j in count: # O(1)
      if count[ord(j)] != 0:
        return False      
    return True