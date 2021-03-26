# coding=utf-8

# Created on 
# Code Jam 2017 qr c
# @author: manolo

import sys

ifile = sys.stdin
ofile = sys.stdout


def r():
    return ifile.readline()[:-1]


def w(case, what):
    ofile.write('Case #{}: {}\n'.format(case, what))


def string(stalls, clients):
    return '{}-{}'.format(','.join(map(str, stalls)), clients)


def solve(stalls, clients):

    comb = []

    while True:

        comb.append(string(stalls, clients))
        print comb

        n = max(stalls)
        stalls.remove(n)

        n_ = n / 2
        if clients == 1:
            if n == 1:
                return 0, 0
            if n == 2:
                return 1, 0
            if n % 2 != 0:
                return n_, n_
            else:
                return n_, n_ - 1

        if n % 2 != 0:
            stalls.extend([n_, n_])
        else:
            stalls.extend([n_ - 1, n_])

        clients -= 1

known = {}

T = int(r())
for case in range(1, T+1):
    n, k = r().split(' ')
    what = solve([int(n)], int(k))
    w(case, '{} {}'.format(*what))

