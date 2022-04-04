# coding=utf-8

# Code Jam 2022
# Round QR
# Problem A
# @author: manolo

from sys import stdin, stdout


def read_line():
    return stdin.readline()[:-1]


def read_one_int_line():
    return int(read_line())


def read_int_line():
    return [int(x) for x in read_line().split(' ')]


def write(case, what):
    stdout.write('Case #{}:\n{}\n'.format(case, what))


def solve(r, c):
    return '\n'.join(['\n'.join([''.join(['..', '-'.join('+' * c)]),
                                 ''.join(['..', '.'.join('|' * c)]),
                                 ]),
                      ''.join([''.join(['-'.join('+' * (c + 1)),
                                        '\n',
                                        '.'.join('|' * (c + 1)),
                                        '\n'
                                        ]) * (r - 1),
                               '-'.join('+' * (c + 1))])])


T = read_one_int_line()
for case in range(1, T + 1):
    r, c = read_int_line()
    what = solve(r, c)
    write(case, what)
