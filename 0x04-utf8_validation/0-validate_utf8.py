#!/usr/bin/python3
"""Module '0-validate_utf8.py' """


def extract_and_count_bits(first_byte):
    """Gets the number of bytes based on the starting bit pattern
    and extracts the rest of the bits

    Args:
        first_byte: Integer representing the first byte of sequence
    Returns:
        tuple: (number of bytes in sequence, extracted bits)
        (-1, 0) if invalid
    """
    if not isinstance(first_byte, int) or first_byte < 0 or first_byte > 0xFF:
        return (-1, 0)

    if (first_byte & 0x80) == 0:
        return (1, first_byte & 0x7F)
    if (first_byte & 0xE0) == 0xC0:  # Check specifically for 110xxxxx
        return (2, first_byte & 0x1F)
    if (first_byte & 0xF0) == 0xE0:
        return (3, first_byte & 0x0F)
    if (first_byte & 0xF0) == 0xF0:  # Check specifically for 11110xxx
        return (4, first_byte & 0x07)
    return (-1, 0)


def extract_following_bits(following_byte):
    """Extracts bits from continuation byte

    Args:
        following_byte: Integer representing a continuation byte
    Returns:
        tuple: (1, extracted bits) if valid, (-1, 0) if invalid
    """
    if (
        not isinstance(following_byte, int)
        or following_byte < 0
        or following_byte > 0xFF
    ):
        return (-1, 0)
    if (following_byte & 0xC0) == 0x80:
        return (1, following_byte & 0x3F)
    return (-1, 0)


def validate_range(data, n_bytes):
    """Validates if a code point is valid according to UTF-8 rules

    Args:
        code_point: Integer value of assembled code point
        n_bytes: Number of bytes used in encoding
    Returns:
        bool: True if valid, False otherwise
    """
    # Check for invalid Surrogate halves
    if 0xD800 <= data <= 0xDFFF:
        return False
    if data > 0x10FFFF:
        return False
    if n_bytes == 2 and data < 0x80:
        return False
    if n_bytes == 3 and data < 0x800:
        return False
    if n_bytes == 4 and data < 0x10000:
        return False
    return True


def validUTF8(data):
    """Validates UTF-8 encoded data
    <https://datatracker.ietf.org/doc/html/rfc3629#page-4>
    Args:
        data: List of integers representing bytes
    Returns:
        bool: True if data is valid UTF-8, False otherwise
    """
    if not data:
        return False

    i = 0
    while i < len(data):
        n_bytes, first_bits = extract_and_count_bits(data[i])

        if n_bytes == -1:
            return False

        if (i + n_bytes) > len(data):
            return False

        # Assemble and validate the code point
        assembled_code = first_bits
        for j in range(i + 1, i + n_bytes):
            status, bits = extract_following_bits(data[j])
            if status == -1:
                return False
            assembled_code = (assembled_code << 6) | bits

        # if not validate_range(assembled_code, n_bytes):
        #     return False

        i += n_bytes

    return True
