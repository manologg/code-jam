# coding=utf-8

# Created on 2016-05-08
# Code Jam 2016 - 1C - C
# @author: manolo


import sys
from itertools import permutations

ifile = sys.stdin
ofile = sys.stdout


def r():
    return ifile.readline()[:-1]


def w(case, what):
    ofile.write('Case #{}: {}\n'.format(case, what))


def create_combinations(a, b, c):
    comb = []
    for ai in range(1, a+1):
        for bi in range(1, b+1):
            for ci in range(1, c+1):
                comb.append((ai, bi, ci))
    return comb


def allowed(outfit, worn, k):

    ab_par = 0
    ac_par = 0
    bc_par = 0

    # print '......START......'

    # print 'outfit', outfit
    # print 'worn', worn

    for worn_outfit in worn:

        # print '............'
        #
        # print '  outfit', outfit
        # print '  worn_outfit', worn_outfit

        same_a = worn_outfit[0] == outfit[0]
        same_b = worn_outfit[1] == outfit[1]
        same_c = worn_outfit[2] == outfit[2]

        # print '  same_a', same_a
        # print '  same_b', same_b
        # print '  same_c', same_c

        if same_a and same_b:
            ab_par += 1
        if same_a and same_c:
            ac_par += 1
        if same_b and same_c:
            bc_par += 1

        # print '  ab_par', ab_par
        # print '  ac_par', ac_par
        # print '  bc_par', bc_par

        if ab_par >= k or ac_par >= k or bc_par >= k:
            # print 'not allowed'
            return False

    # print 'allowed'
    return True


def solve(comb, max):

    worn = []

    for outfit in comb:
        if allowed(outfit, worn, max):
            worn.append(outfit)

    return worn


T = int(r())
for case in range(1, T+1):
    a, b, c, max = [int(c) for c in r().split(' ')]
    comb = create_combinations(a, b, c)
    # print '----------------------'
    # print '{} - {} - {} ({})'.format(a, b, c, max)
    solution = []
    for combination in permutations(comb):
        worn = solve(comb, max)
        if len(worn) > len(solution):
            solution = worn

    # print worn
    what = '{}'.format(len(worn))
    for outfit in worn:
        what += '\n{} {} {}'.format(outfit[0], outfit[1], outfit[2])
    w(case, what)

