'''
05.07 airwise Swap: Write a program to swap odd and even bits in an integer with as few instructions as
    possible (e.g., bit 0 and bit 1 are swapped, bit 2 and bit 3 are swapped, and so on).
'''

# Time: O(1) Space: O(1)
def pairwise_swap(number):
    mask_10 = 0xAAAAAAAA  # 32 bits
    mask_01 = 0x55555555  # 32 bits
    num_evn = number & mask_10
    num_odd = number & mask_01
    swp_num = (num_evn >> 1) | (num_odd << 1)
    return swp_num