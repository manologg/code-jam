# coding=utf-8
"""
Created on 11/04/2015
Code Jam 2015 QR c
@author: manolo
"""

import sys

ifile = sys.stdin
ofile = open('./c.out', 'w')


def r():
    return ifile.readline()[:-1]


def w(case, what):
    ofile.write('Case #{}: {}\n'.format(case, what))
    print 'Case #{}: {}\n'.format(case, what)


YES = 'YES'
NO = 'NO'

vals = dict()
vals['11'] = '1'
vals['1i'] = 'i'
vals['1j'] = 'j'
vals['1k'] = 'k'

vals['i1'] = 'i'
vals['ii'] = '-1'
vals['ij'] = 'k'
vals['ik'] = '-j'

vals['i1'] = 'j'
vals['ji'] = '-k'
vals['jj'] = '-1'
vals['jk'] = 'i'

vals['i1'] = 'k'
vals['ki'] = 'j'
vals['kj'] = '-i'
vals['kk'] = '-1'


def apply_rules(str):

    for v in vals:
        str = str.replace(v, vals[v])

    return str


def reduce(str):

    minus = 0

    while True:
        new_str = apply_rules(str)

        if new_str == str:  # no change at all, break the loop
            break

        minus += new_str.count('-')
        str = new_str.replace('-', '')
        print 'str: "{}" // minus: {}'.format(str, minus)

    if minus % 2 == 1:
        return '-' + str
    else:
        return str


def solve(str, x):

    print 'reducing "{}"...'.format(str)
    str = reduce(str)
    print 'reduced: "{}"'.format(str)

    if str == x:
        return YES
    else:
        return NO


def wait_for(str, x):

    if str[0] == x:
        return 0

    negative = False
    current = str[0]

    for i in range(1, len(str)):
        print '{} * {}'.format(current, str[i])

        current = vals[current + str[i]]

        if current == x:
            return i

        if '-' in current:
            negative = not negative
            current = current[1]

        print ' = {}'.format(current)

    return -1


def solve2(str):
    for_i = wait_for(str, 'i')
    for_i =  wait_for(str, 'i')
    for_i = wait_for(str, 'i')


T = int(r())
for case in range(1, T + 1):
    l, x = r().split(' ')
    str = r()

    what = solve2(str * int(x))
    w(case, what)

ofile.close









