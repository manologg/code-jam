# coding=utf-8
"""
Created on 11/04/2015
Code Jam 2015 QR b
@author: manolo
"""

import sys

ifile = sys.stdin
ofile = open('./b_old2.out', 'w')


def r():
    return ifile.readline()[:-1]


def w(case, what):
    ofile.write('Case #{}: {}\n'.format(case, what))


def solve(pancackes):

    best_time = sys.maxint
    special_minutes = 0

    while True:

        max_pancackes = max(pancackes)

        max_time = max_pancackes + special_minutes

        print 'pancackes: {}'.format(pancackes)
        print 'best time: {}'.format(best_time)
        print 'max of minutes now: {} + {} = {}'.format(max_pancackes, special_minutes, max_time)

        if max_time < best_time:
            best_time = max_time

        if max_pancackes == 1:
            break

        print '-'
        special_minutes += 1
        print '{}. special minute!'.format(special_minutes)
        pancackes.remove(max_pancackes)
        half_of_max_pancackes = max_pancackes / 2
        pancackes.append(half_of_max_pancackes)
        if max_pancackes % 2:  # uneven number
            pancackes.append(half_of_max_pancackes + 1)
        else:
            pancackes.append(half_of_max_pancackes)

    print '-----\n'

    return best_time


T = int(r())
for case in range(1, T+1):

    diners = r()
    pancackes = r().split(' ')
    print 'Case #{}: {}'.format(case, map(int, pancackes))
    what = solve(map(int, pancackes))
    w(case, what)


ofile.close


