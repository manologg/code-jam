# coding=utf-8
"""
Created on 11/04/2015
Code Jam 2015 QR b
@author: manolo
"""

import sys

ifile = sys.stdin
ofile = open('./b_new.out', 'w')


def r():
    return ifile.readline()[:-1]


def w(case, what):
    ofile.write('Case #{}: {}\n'.format(case, what))
    #print 'Case #{}: {}\n'.format(case, what)


def solve(pancackes, minutes=0):

    global best_time

    #print '{}pancackes: {}'.format('\t' * minutes, pancackes)
    #print '{}best time: {}'.format('\t' * minutes, best_time)
    #print '{}minutes: {}'.format('\t' * minutes, minutes)

    if not pancackes:
        #print '{}-- {} min --'.format('\t' * minutes, minutes)
        return minutes

    # important, everywhere
    max_pancackes = max(pancackes)

    if max_pancackes == 0:
        #print '{}-- {} min --'.format('\t' * minutes, minutes)
        return minutes

    if minutes >= best_time:
        #print '{}-- X --'.format('\t' * minutes)
        return best_time

    # eat the rest
    letting_eat_time = minutes + max_pancackes
    #print '{}letting them eat now: {}'.format('\t' * (minutes+1), letting_eat_time)

    if letting_eat_time < best_time:
        #print '{}best time! {}'.format('\t' * (minutes+1), letting_eat_time)
        best_time = letting_eat_time

    #print

    # time flies...
    minutes += 1

    # special minute
    if max_pancackes != 1:
        new_pancackes = list(pancackes)
        new_pancackes.remove(max_pancackes)
        half_of_max_pancackes = max_pancackes / 2
        new_pancackes.append(half_of_max_pancackes)
        if max_pancackes % 2:  # uneven number
            new_pancackes.append(half_of_max_pancackes + 1)
        else:
            new_pancackes.append(half_of_max_pancackes)

        #print '{}special minute: {} --> {}'.format('\t' * minutes, pancackes, new_pancackes)
        special_time = solve(new_pancackes, minutes)

        if special_time < best_time:
            #print '{}best time! {}'.format('\t' * minutes, special_time)
            best_time = special_time

        #print

    # eat pancackes
    new_pancackes = list()
    for x in pancackes:
        if x > 1:
            new_pancackes.append(x-1)

    #print '{}every one eats a pancacke {} --> {}'.format('\t' * minutes, pancackes, new_pancackes)
    eat_time = solve(new_pancackes, minutes)

    if eat_time < best_time:
        #print '{}best time! {}'.format('\t' * minutes, eat_time)
        best_time = eat_time

    return best_time


T = int(r())
for case in range(1, T+1):

    diners = r()
    pancackes = r().split(' ')
    pancackes = map(int, pancackes)
    #print 'Case #{}: {}'.format(case, pancackes)
    best_time = max(pancackes)
    what = solve(pancackes)
    w(case, what)


ofile.close



