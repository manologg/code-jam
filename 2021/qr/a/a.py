# coding=utf-8

# Code Jam 2021
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
    stdout.write(f'Case #{case}: {what}\n')


def solve(n, l):
    cost = 0
    for i in range(n-1):
        n = min(l[i:])
        j = l.index(n, i)
        start = l[:i]
        middle = list(reversed(l[i:j+1]))
        end = l[j+1:]
        l = start + middle + end
        cost += len(middle)
    return cost


T = read_one_int_line()
for case in range(1, T + 1):
    n = read_one_int_line()
    l = read_int_line()
    what = solve(n, l)
    write(case, what)
