'''
1.5 One Away: There are three types of edits that can be performed on strings: insert a character, 
remove a character, or replace a character. Given two strings, write a function to check if they are 
one edit (or zero edits) away. 
EXAMPLE 
ple, pale -> true 
pales. pale -> true 
pale. bale -> true 
pale. bake -> false 
'''
#Time: O(n) Space: O(1)
def oneAway(str1, str2):
    x = len(str1)
    y = len(str2)    
    if abs(x - y)>1:
        return False
    i = 0
    j = 0
    count = 0
    while i < x and j < y:
        if str1[i]!= str2[j]:
            if x > y:
                i += 1
            elif x < y:
                j += 1
            else:
                i += 1
                j += 1
            count += 1
        else:
            i += 1
            j += 1            
    if count > 1:
        return False
    else:
        return True