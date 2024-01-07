#!/usr/bin/python3
"""determines if a given data set represents a valid UTF-8 encoding"""


def validUTF8(data):
    """determines if a given data set represents a valid UTF-8 encoding"""
    bytes_to_process = 0
    for num in data:
        num = format(num, '#010b')[-8:]
        if bytes_to_process == 0:
            for bit in num:
                if bit == '0':
                    break
                bytes_to_process += 1
            if bytes_to_process == 0:
                continue
            if bytes_to_process == 1 or bytes_to_process > 4:
                return False
        else:
            if not (num[0] == '1' and num[1] == '0'):
                return False
        bytes_to_process -= 1
    return bytes_to_process == 0
