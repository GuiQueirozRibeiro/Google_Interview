'''
05.06 Conversion: Write a function to determine the number of bits you would need to flip to convert
    integer A to integer B.

    EXAMPLE

    Input: 29 (or: 11101), 15 (or: 01111)
    Output: 2
'''

# Time: O(n) Space: O(1)
def bit_swap_required(a: int, b: int) -> int:
    count, c = 0, a ^ b
    while c:
        count, c = count + 1, c & (c - 1)
    return count