# coding=utf-8

# Code Jam 2021
# Round QR
# Problem B
# @author: manolo

from sys import stdin, stdout


def read_line():
    return stdin.readline()[:-1]


def read_one_int_line():
    return int(read_line())


def write(case, what):
    stdout.write(f'Case #{case}: {what}\n')


def solve(x, y, w):
    w = [c for c in w if c != '?']
    if len(w) < 2:
        return 0
    last = w[0]
    cost = 0
    for c in w[1:]:
        if c == last:
            continue

        elif last == 'C' and c == 'J':
            cost += x
        else:
            cost += y

        last = c

    return cost


T = read_one_int_line()
for case in range(1, T + 1):
    x, y, word = read_line().split(' ')
    what = solve(int(x), int(y), word)
    write(case, what)
