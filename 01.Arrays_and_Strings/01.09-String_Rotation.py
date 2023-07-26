'''
01.09 String Rotation: Assume you have a method isSubst ring which checks if one word is a substring
    of another. Given two strings, 51 and 52, write code to check if 52 is a rotation of 51 using only one
    call to isSubstring (e.g., "waterbottle" is a rotation of"erbottlewat").
'''

# Time: O(b+s) Space: O(b+s)
def isSubstring(B, S):
    hash = []
    b = len(B)
    s = len(S)
    q = 11
    v = 128
    prevHashValue = 0
    hashValue = 0
    for i in range(s):
        prevHashValue = (v*prevHashValue + ord(S[i]))%q
        hashValue = (v*hashValue + ord(B[i]))%q   
    for i in range(b-s+1):
        if hashValue == prevHashValue:
            match = True
            for j in range(s):
                if B[i+j] != S[j]:
                    match = False
                    break
            if match:
                hash = hash +[i]
        if i<b-s:
            hashValue = (v*(hashValue-ord(B[i]))+ord(B[i+s])) % q       
    if hash != []:
        return True
    else:
        return False
          
def stringRotation(s1 ,s2):
    if len(s1) != len(s2):
        return False 
    else:
        return isSubstring(s1+s1, s2);