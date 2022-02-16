# coding=utf-8

# Code Jam 2021
# Round QR
# Problem C
# @author: manolo


from itertools import permutations
from sys import stdin, stdout


def read_line():
    return stdin.readline()[:-1]


def read_one_int_line():
    return int(read_line())


def read_int_line():
    return [int(x) for x in read_line().split(' ')]


def write(case, what):
    stdout.write('Case #{}: {}\n'.format(case, what))


def calculate_cost(n, l, max_cost):
    cost = 0
    for i in range(n - 1):
        n = min(l[i:])
        j = l.index(n, i)
        start = l[:i]
        middle = list(reversed(l[i:j + 1]))
        end = l[j + 1:]
        l = start + middle + end
        cost += len(middle)
        if cost > max_cost:
            return cost
    return cost


def solve(n, c):
    all = permutations(range(1, n + 1), n)
    for l in all:
        cost = calculate_cost(n, list(l), c)
        if cost == c:
            return ' '.join([str(x) for x in l])

    return 'IMPOSSIBLE'


T = read_one_int_line()

for case in range(1, T + 1):
    n, c = read_int_line()
    what = solve(n, c)
    write(case, what)
