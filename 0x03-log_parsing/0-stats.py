#!/usr/bin/python3
"""Module '0-stats.py' contains scripts that reads stdin
line by line and computes metrics """
import os
import re
import sys


pattern = (
    r"^(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\s-\s"
    r"\[(\d{4}-\d{2}-\d{2}\s\d{2}:\d{2}:\d{2}\.\d{6})\]\s"
    r'"(?:GET\s/projects/\d+\sHTTP/1\.1)"\s'
    r"(?P<status>\d{3})\s"
    r"(?P<size>\d+)$"
)


def parse_line(line: str):
    """Checks if line matches pattern, get and returns
    the http status code and the size of the file"""
    match = re.match(pattern, line)
    if not match:
        return None
    status = int(match.group("status"))
    size = int(match.group("size"))
    return status, size


def print_stats(total_file_size: int, request_frequency: {}, no_of_lines: int):
    """Prints stats in desired format"""
    print("File size: {}".format(total_file_size))
    for code in sorted(request_frequency):
        print("{}: {}".format(code, request_frequency[code]))


def main():
    """Runs the main function"""
    total_file_size = 0
    request_frequency = {}
    no_of_lines = 0
    try:
        for line in sys.stdin:
            line = line.rstrip()
            # check line format with regex
            data = parse_line(line)
            if data is not None:
                if data[0] not in request_frequency:
                    request_frequency[data[0]] = 1
                else:
                    request_frequency[data[0]] += 1
                total_file_size += data[1]
                # after every ten lines or CTRL + C, print stats
                no_of_lines += 1
                if no_of_lines % 10 == 0:
                    print_stats(total_file_size, request_frequency, no_of_lines)
    except (KeyboardInterrupt, EOFError):
        pass
    finally:
        print_stats(total_file_size, request_frequency, no_of_lines)


if __name__ == "__main__":
    main()
