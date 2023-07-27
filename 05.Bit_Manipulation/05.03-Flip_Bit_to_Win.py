'''
05.03 Flip Bit to Win: You have an integer and you can flip exactly one bit from a 0 to a 1. Write code to
    find the length of the longest sequence of ls you could create.

    EXAMPLE

    Input: 1775 (or: 11011101111)
    Output: 8
'''

# Time: O(n) Space: O(1)
def flip_bit_to_win(num):
    longest, current_segment, past_segment = 1, 0, 0
    while num != 0:
        if num & 1:
            current_segment += 1
        else:
            past_segment = 0 if (num & 2 is True) else current_segment
            current_segment = 0
        longest = max(current_segment + past_segment + 1, longest)
        num >>= 1
    return longest