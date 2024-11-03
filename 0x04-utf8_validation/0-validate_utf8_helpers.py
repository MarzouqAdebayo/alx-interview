#!/usr/bin/python3
"""Module '0-validate_utf8_helpers.py' """


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
