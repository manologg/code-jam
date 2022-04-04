# coding=utf-8

# Code Jam 2022
# Round QR
# Problem B
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


def solve(c0, m0, y0, k0, c1, m1, y1, k1, c2, m2, y2, k2):
    c = min(c0, c1, c2)
    m = min(m0, m1, m2)
    y = min(y0, y1, y2)
    k = min(k0, k1, k2)

    colors = [c, m, y, k]

    if sum(colors) < 1_000_000:
        return 'IMPOSSIBLE'

    for i in range(4):

        if sum(colors) == 1_000_000:
            break
        else:
            rest_sum = sum(colors[i + 1:])
            if rest_sum < 1_000_000:
                colors[i] = 1_000_000 - rest_sum
            else:
                colors[i] = 0

    if sum(colors) < 1_000_000:
        return 'IMPOSSIBLE'

    return ' '.join([str(x) for x in colors])


if __name__ == '__main__':
    T = read_one_int_line()
    for case in range(1, T + 1):
        p0 = read_int_line()
        p1 = read_int_line()
        p2 = read_int_line()
        what = solve(*p0, *p1, *p2)
        write(case, what)
