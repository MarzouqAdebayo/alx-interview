#!/usr/bin/python3
"""Module '0-validate_utf8.py' """


def extract_and_count_bits(first_byte):
    """Gets the number of bytes on based on the
    starting bit in arg first_byte and
    extract the rest of the bits"""
    one_byte_mask = 0x80  # 0b10000000
    two_byte_mask = 0xC0  # 0b11000000
    three_byte_mask = 0xE0  # 0b11100000
    four_byte_mask = 0xF0  # 0b11110000
    if (first_byte & one_byte_mask) == 0:
        return (1, first_byte & 0x3F)
    if (first_byte & two_byte_mask) == two_byte_mask:
        return (2, first_byte & 0x1F)
    if (first_byte & three_byte_mask) == three_byte_mask:
        return (3, first_byte & 0x0F)
    if (first_byte & four_byte_mask) == four_byte_mask:
        return (4, first_byte & 0xF)
    return (-1, 0)


def extract_following_bits(following_byte):
    """Extracts following bits"""
    one_byte_mask = 0x80  # 0b10000000
    following_bytes_mask = 0xC0  # 0b11000000
    if (following_byte & following_bytes_mask) == one_byte_mask:
        return (1, following_byte & 0x3F)
    return (-1, 0)


def validUTF8(data):
    """Validates utf8 data
    <https://datatracker.ietf.org/doc/html/rfc3629#page-4>
    """
    i = 0
    while i < len(data):
        if data[i] is not int or data[i] < 0 or data[i] > 0x10FFFF:
            return False
        (n_bytes, _) = extract_and_count_bits(data[i])

        if n_bytes == -1:
            return False
        if (i + n_bytes) > len(data):
            return False
        for j in range(i + 1, i + n_bytes):
            if data[j] is not int or data[j] < 0 or data[j] > 0x10FFFF:
                return False
            (current_byte_count, _) = extract_following_bits(data[j])
            if current_byte_count == -1:
                return False
        i += n_bytes
    return True
