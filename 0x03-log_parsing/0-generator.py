#!/usr/bin/python3
import random
import sys
from time import sleep
import datetime

for i in range(11):
    sleep(random.random())
    if i % 3 == 0:
        sys.stdout.write(
            '{:d}.{:d}.{:d}.{:d} - [{}] "GET /projects/260 HTTP/1.1" {} {}\n'.format(
                random.randint(1, 255),
                random.randint(1, 255),
                random.randint(1, 255),
                random.randint(1, 255),
                datetime.datetime.now(),
                # random.choice([200, 301, 400, 401, 403, 404, 405, 500, 677]),
                random.choice([205, 305, 409, 408, 413, 224, 333, 677]),
                random.randint(1, 1024),
            )
        )
    else:
        sys.stdout.write(
            '{:d}.{:d}.{:d}.{:d} - [{}] "GET /projects/260 HTTP/1.1" {} {}\n'.format(
                random.randint(1, 255),
                random.randint(1, 255),
                random.randint(1, 255),
                random.randint(1, 255),
                datetime.datetime.now(),
                # random.choice([200, 301, 400, 401, 403, 404, 405, 500, 677]),
                random.choice([205, 305, 409, 408, 413, 224, 333, 677]),
                random.randint(1, 1024),
            )
        )
    sys.stdout.flush()
