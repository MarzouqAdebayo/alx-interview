#!/usr/bin/python3
"""Module '0-validate_utf8.py' """


def get_number_of_bytes(first_byte):
    """Gets the number of bytes on based on the
    starting bit in arg first_byte"""
    one_byte_mask = 0x80  # 0b10000000
    two_byte_mask = 0xC0  # 0b11000000
    three_byte_mask = 0xE0  # 0b11100000
    four_byte_mask = 0xF0  # 0b11110000
    if (first_byte & one_byte_mask) == 0:
        return 1
    if (first_byte & two_byte_mask) == two_byte_mask:
        return 2
    if (first_byte & three_byte_mask) == three_byte_mask:
        return 3
    if (first_byte & four_byte_mask) == four_byte_mask:
        return 4
    return -1


def validUTF8(data):
    """Checks if all characters in data is valid UTF8
    A valid UTF8 encoded data must meet these 3 criteria
    1. If number of bytes returned by the initial bits of the first byte
    is invalid i.e between 1 to 4 bytes and is invalid (check function
    get_number_of_bytes() i.e (b10xxxxxx or b1100xxxx)
    2. If the number of bytes in data is greater that the number of bytes
    set in the bits of the first byte (Someone is lying :)
    3. If the following bytes dont start with bits (1 and 0) b10xxxxxx
    """
    one_byte_mask = 0x80  # 0b10000000
    following_bytes_mask = 0xC0  # 0b11000000
    i = 0
    if len(data) == 0:
        return False

    n_bytes = get_number_of_bytes(data[i])
    if n_bytes == -1:
        return False

    if i + n_bytes > len(data):
        return False

    for j in range(i + 1, i + n_bytes):
        if (data[j] & following_bytes_mask) != one_byte_mask:
            return False
    return True
