# coding=utf-8

# Code Jam 2022
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


def solve(dice):
    dice = sorted(dice)
    i = 0
    while i < len(dice):
        if dice[i] < i + 1:
            dice = dice[:i] + dice[i + 1:]
        else:
            i += 1

    return len(dice)


if __name__ == '__main__':
    T = read_one_int_line()
    for case in range(1, T + 1):
        n = read_int_line()
        dice = read_int_line()
        what = solve(dice)
        write(case, what)
