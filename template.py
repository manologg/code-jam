# coding=utf-8

# Code Jam 2021
# Round QR
# Problem C
# @author: manolo

from sys import stdin, stdout


def read_line():
    return stdin.readline()[:-1]


def read_one_int_line():
    return int(read_line())


def read_int_line():
    return [int(x) for x in read_line().split(' ')]


def write(case, what):
    stdout.write('Case #{}: {}\n'.format(case, what))


def solve(e, r, n):
    return 0


T = read_one_int_line()
for case in range(1, T + 1):
    # e, r, n = read_int_line()
    # what = solve(e, r, n)
    x, y, word = read_line().split(' ')
    what = solve(int(x), int(y), word)
    write(case, what)
