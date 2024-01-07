#!/usr/bin/python3
from sys import argv as av
if __name__ == '__main__':
    ac = len(av) - 1
    sum = 0

    if ac > 0:
        for i in range(1, len(av), 1):
            sum += int(av[i])
    print('{}'.format(sum))
