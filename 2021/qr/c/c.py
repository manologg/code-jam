# coding=utf-8

# Code Jam 2021
# Round QR
# Problem C
# @author: manolo

from sys import stdin, stdout


def read_line():
    return stdin.readline()[:-1]


def read_one_int_line():
    return int(read_line()[:-1])


def read_int_line():
    return [int(x[:-1]) for x in read_line().split(' ')]


def write(case, what):
    stdout.write('Case #{}: {}\n'.format(case, what))


def solve(e, r, n):
    return 0


T = read_one_int_line()
for case in range(1, T + 1):
    e, r, n = read_int_line()
    what = solve(e, r, n)
    write(case, what)
