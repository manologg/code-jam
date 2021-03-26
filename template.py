# coding=utf-8

# Code Jam <YEAR>
# Round <ROUND>
# Problem <PROBLEM>
# @author: manolo

from sys import stdin, stdout


def read_line():
    return stdin.readline()[:-1]


def read_one_int_line():
    return int(read_line())


def read_int_line():
    return [int(x) for x in read_line().split(' ')]


def write(case, what):
    stdout.write(f'Case #{case}: {what}\n')


def solve(n, l):
    pass


T = read_one_int_line()
for case in range(1, T + 1):
    n = read_one_int_line()
    l = read_int_line()
    what = solve(n, l)
    write(case, what)
