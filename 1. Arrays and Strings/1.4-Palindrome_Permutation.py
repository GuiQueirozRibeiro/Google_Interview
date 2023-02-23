'''
1.4 Palindrome Permutation: Given a string, write a function to check if it is a permutation of a palindrome. A palindrome is a word or phrase that is the same forwards and backwards. A permutation 
is a rearrangement of letters. The palindrome does not need to be limited to just dictionary words.
EXAMPLE 
Input: tactcoa 
Output: True (permutations: "tacocat". "atcocta". etc.) 
'''
#Time: O(n) Space: O(1)
def Palindrome(str):
    dicio = {}
    count = 0
    for i in str:
        if (i in dicio):
            dicio[i] += 1
        else:
            dicio[i] = 1
    x = len(str)%2
    if x == 0:
        for i in dicio:
            if dicio[i]%2 != 0:
                return False  
        return True
    else: 
        for i in dicio:
            if dicio[i]%2 != 0:
                count += 1     
            if count > 1:
                return False
            return True