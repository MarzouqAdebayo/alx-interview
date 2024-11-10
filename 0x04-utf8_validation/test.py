#!/usr/bin/env python3


# get_number_of_bytes = __import__("0-validate_utf8").get_number_of_bytes
validUTF8 = __import__("0-validate_utf8").validUTF8
data = [65]
print(validUTF8(data))

data = [
    80,
    121,
    116,
    104,
    111,
    110,
    32,
    105,
    115,
    32,
    99,
    111,
    111,
    108,
    33,
]
print(validUTF8(data))

data = [229, 65, 127, 256]
print(validUTF8(data))

data = [24, "hey", 20000000000000000000000000000000, 22, "hello", "stop"]
print(validUTF8(data))

data = [0xF8]
print(validUTF8(data))
