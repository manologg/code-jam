# coding=utf-8
"""
Created on 11/04/2015
Code Jam 2015 QR b
@author: manolo
"""

import sys

ifile = sys.stdin
ofile = open('./b.out', 'w')


def r():
    return ifile.readline()[:-1]


def w(case, what):
    ofile.write('Case #{}: {}\n'.format(case, what))


def solve(e, r, n):
    return 0


T = int(r())
for case in range(1, T + 1):
#    e, r, n = r().split(' ')
#    what = solve(int(e), int(r), int(n)
#    w(case, what)


ofile.close


