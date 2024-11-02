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
    if not isinstance(first_byte, int) or first_byte < 0:
        return (-1, 0)

    byte = first_byte & 0xFF

    if (byte & 0x80) == 0:
        return (1, byte & 0x7F)
    if (byte & 0xE0) == 0xC0:
        return (2, byte & 0x1F)
    if (byte & 0xF0) == 0xE0:
        return (3, byte & 0x0F)
    if (byte & 0xF8) == 0xF0:
        return (4, byte & 0x07)
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


def validUTF8(data):
    """Validates UTF-8 encoded data
    <https://datatracker.ietf.org/doc/html/rfc3629#page-4>
    Args:
        data: List of integers representing bytes
    Returns:
        bool: True if data is valid UTF-8, False otherwise
    """
    if not data or len(data) == 0:
        return True

    i = 0
    while i < len(data):
        n_bytes, first_bits = extract_and_count_bits(data[i])

        if n_bytes == -1:
            return False

        if (i + n_bytes) > len(data):
            return False

        for j in range(i + 1, i + n_bytes):
            status, bits = extract_following_bits(data[j])
            if status == -1:
                return False

        i += n_bytes

    return True
