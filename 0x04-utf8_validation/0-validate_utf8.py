#!/usr/bin/python3
"""Module '0-validate_utf8.py' """


def extract_and_count_bits(first_byte):
    """Gets the number of bytes on based on the
    starting bit in arg first_byte and
    extract the rest of the bits"""
    if not isinstance(first_byte, int) or first_byte < 0 or first_byte > 0x10FFFF:
        return (-1, 0)
    one_byte_mask = 0x80  # 0b10000000
    two_byte_mask = 0xC0  # 0b11000000
    three_byte_mask = 0xE0  # 0b11100000
    four_byte_mask = 0xF0  # 0b11110000
    if (first_byte & one_byte_mask) == 0:
        return (1, first_byte & 0x7F)
    if (first_byte & two_byte_mask) == two_byte_mask:
        return (2, first_byte & 0x1F)
    if (first_byte & three_byte_mask) == three_byte_mask:
        return (3, first_byte & 0x0F)
    if (first_byte & four_byte_mask) == four_byte_mask:
        return (4, first_byte & 0x07)
    return (-1, 0)


def extract_following_bits(following_byte):
    """Extracts following bits"""
    if (
        not isinstance(following_byte, int)
        or following_byte < 0
        or following_byte > 0xFF
    ):
        return (-1, 0)
    continuation_mask = 0xC0  # 0b11000000
    if (following_byte & continuation_mask) == 0x80:
        return (1, following_byte & 0x3F)
    return (-1, 0)


def validate_range(data):
    """Validates if the assembled data is valid according to UTF-8 rules"""
    # Check for surrogate halves (U+D800 through U+DFFF)
    if 0xD800 <= data <= 0xDFFF:
        return False

    # Check maximum allowed code point
    if data > 0x10FFFF:
        return False

    return True


def validUTF8(data):
    """Validates utf8 data
    <https://datatracker.ietf.org/doc/html/rfc3629#page-4>
    Args:
        data: List of integers representing bytes
    Returns:
        bool: True if data is valid UTF-8, False otherwise
    """
    if not data:
        return True
    i = 0
    while i < len(data):
        (n_bytes, first_bits) = extract_and_count_bits(data[i])
        # print(f"Index {i}: n_bytes = {n_bytes}")

        if n_bytes == -1:
            print(f"Invalid start byte at index {i}: {data[i]}")
            return False
        if n_bytes == 2 and first_bits <= 0x01:
            return False
        if n_bytes == 3 and first_bits == 0:
            return False
        if n_bytes == 4 and first_bits == 0:
            return False

        if (i + n_bytes) > len(data):
            # print("Insufficient bytes for UTF-8 character")
            return False

        assembled_code = first_bits
        for j in range(i + 1, i + n_bytes):
            (current_byte_count, bits) = extract_following_bits(data[j])
            # print(
            #     f"Index {j}: following_byte = {data[j]}, current_byte_count \
            #     = {current_byte_count}"
            # )
            if current_byte_count == -1:
                # print(f"Invalid following byte at index {j}: {data[j]}")
                return False
            assembled_code = (assembled_code << 6) | bits

        if not validate_range(assembled_code):
            return False

        i += n_bytes
    return True
