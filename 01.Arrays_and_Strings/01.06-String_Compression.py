'''
01.06 String Compression: Implement a method to perform basic string compression using the counts
    of repeated characters. For example, the string aabcccccaaa would become a2b1c5a3. If the
    "compressed" string would not become smaller than the original string, your method should return
    the original string. You can assume the string has only uppercase and lowercase letters (a - z).
'''

#Time: O(n) Space: O(n)

def compress(string):
    compress_string = ""
    letter = ""
    count = 0
    for char in string:
        if char == letter:
            count += 1
        else:
            if count > 0:
                compress_string += letter + str(count)
            letter = char
            count = 1
    compress_string += letter + str(count)
    if len(string) > len(compress_string):
        return compress_string
    else:
        return string