"""
    The following program tests and prints the size of a list while adding elements dynamically
"""
from sys import getsizeof

def experiment(num):
    data = []
    for i in range(num):
        a = len(data)
        b = getsizeof(data)
        print('Length: {0:3d}; Size in bytes: {1:4d}'.format(a, b))
        data.append(i)

if __name__ == "__main__":
    experiment(27)

    """OUTPUT
    Length:   0; Size in bytes:   64
    Length:   1; Size in bytes:   96
    Length:   2; Size in bytes:   96
    Length:   3; Size in bytes:   96
    Length:   4; Size in bytes:   96
    Length:   5; Size in bytes:  128
    Length:   6; Size in bytes:  128
    Length:   7; Size in bytes:  128
    Length:   8; Size in bytes:  128
    Length:   9; Size in bytes:  192

    """


