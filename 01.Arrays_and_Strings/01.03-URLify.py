'''
01.03 URLify: Write a method to replace all spaces in a string with "%20" You may assume that the string
      has sufficient space at the end to hold the additional characters, and that you are given the "true"
      length of the string. (Note: If implementing in Java, please use a character array so that you can
      perform this operation in place).

      EXAMPLE

      Input: "Mr John Smith    ", 13
      Output: "Mr%20John%20Smith"
'''

#Time: O(n) Space: O(1)

def urlify(string, length):
    list_str = list(string)
    x = len(list_str)-1
    for i in range(length-1, -1, -1):
        if(list_str[i]!=' '):
            list_str[x] = list_str[i]
            x -= 1
        else:
            list_str[x] = '0'
            list_str[x-1] = '2'
            list_str[x-2] = '%'
            x -= 3
    return "".join(list_str)