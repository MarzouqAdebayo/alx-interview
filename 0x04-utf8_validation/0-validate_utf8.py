#!/usr/bin/python3
"""Module '0-validate_utf8.py' """


extract_and_count_bits = __import__(
    "0-validate_utf8_helpers").extract_and_count_bits
extract_following_bits = __import__(
    "0-validate_utf8_helpers").extract_following_bits


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
