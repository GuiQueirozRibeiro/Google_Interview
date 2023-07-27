'''
05.01 Insertion: You are given two 32-bit numbers, N and M, and two bit positions, i and j.
    Write a method to insert M into N such that M starts at bit j and ends at bit i. You
    can assume that the bits j through i have enough space to fit all of M. That is, if
    M = 10011, you can assume that there are at least 5 bits between j and i. You would not, for
    example, have j = 3 and i = 2, because M could not fully fit between bit 3 and bit 2.

    EXAMPLE

    Input: N = 10000000000, M = 10011, i = 2, j = 6
    Output: N = 10001001100
'''

# Time: O(1) Space: O(1)
def bits_insertion(n, m, i, j):
    ones_left = -1 << (j + 1)
    ones_right = (1 << i) - 1
    mask = ones_left | ones_right
    cleared = n & mask
    moved = m << i
    return cleared | moved