import os
from contextlib import contextmanager

@contextmanager
def open_file(file_name, mode):
    try:
        f = open(file_name, mode)
        yield f
    finally:
        f.close()

with open_file('test.txt', 'w') as f:
    f.write('Hello This is me')

print(f.closed)