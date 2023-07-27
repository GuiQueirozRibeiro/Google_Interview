'''
05.02 Binary to String: Given a real number between O and 1 (e.g., 0.72) that is passed in as a double, print
    the binary representation. If the number cannot be represented accurately in binary with at most 32
    characters, print "ERROR".
'''

# Time: O(1) Space: O(1)
def bin_to_string(number):
    number_s31 = int(number * (2**32))
    if number_s31 > 2**32:
        return "ERROR"

    if number_s31 == (2**32):
        number_s31 = 2**32 - 1

    ans = ""
    for _ in range(32):
        ans = str(number_s31 % 2) + ans
        number_s31 = number_s31 // 2

    return "." + ans