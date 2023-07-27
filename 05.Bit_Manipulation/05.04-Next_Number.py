'''
05.04 Next Number: Given a positive integer, print the next smallest and the next largest number that
    have the same number of 1 bits in their binary representation.
'''

from typing import Optional

# Time: O(n) Space: O(1)

def _bit(x: int, i: int) -> int:
    return x & (1 << i)

def next_smaller(x: int) -> Optional[int]:
    if not x & (x + 1):
        return None
    zeros = ones = 0
    while _bit(x, i=ones):
        ones += 1
    while not _bit(x, i=ones + zeros):
        zeros += 1
    return x - (1 << ones) - (1 << zeros - 1) + 1

def next_larger(x: int) -> int:
    zeros = ones = 0
    while not _bit(x, i=zeros):
        zeros += 1
    while _bit(x, i=zeros + ones):
        ones += 1
    return x + (1 << zeros) + (1 << ones - 1) - 1