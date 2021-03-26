# coding=utf-8

# Created on 
# Code Jam 2017 qr d
# @author: manolo

import sys

ifile = sys.stdin
ofile = sys.stdout


def r():
    return ifile.readline()[:-1]


def w(case, what):
    ofile.write('Case #{}: {}\n'.format(case, what))


def solve(e, r, n):
    return 0

T = int(r())
for case in range(1, T+1):
    e, r, n = r().split(' ')
    what = solve(int(e), int(r), int(n))
    w(case, what)

