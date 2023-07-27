'''
05.08 Draw Line: A monochrome screen is stored as a single array of bytes, allowing eight consecutive
    pixels to be stored in one byte. The screen has width w, where w is divisible by 8 (that is, no byte will
    be split across rows). The height of the screen, of course, can be derived from the length of the array
    and the width. Implement a function that draws a horizontal line from (x1, y) to ( x2, y).
    The method signature should look something like:

    drawline(byte[] screen, int width, int x1, int x2, int y)
'''

# Time: O(x2 - x1) Space: O(1)
def draw_line(screen: bytearray, width: int, x1: int, x2: int, y: int) -> None:
    left_byte, right_byte = (y * width + x1) // 8, (y * width + x2) // 8
    left_mask, right_mask = 0xFF >> x1 % 8, (0xFF >> x2 % 8 + 1) ^ 0xFF
    if left_byte == right_byte:
        screen[left_byte] |= left_mask & right_mask
    else:
        screen[left_byte] |= left_mask
        for i in range(left_byte + 1, right_byte):
            screen[i] = 0xFF
        screen[right_byte] |= right_mask