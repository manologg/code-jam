# coding=utf-8

# Code Jam 2021
# Round QR
# Problem B
# @author: manolo

from sys import stdin, stdout

C = 'C'
J = 'J'


def read_line():
    return stdin.readline()[:-1]


def read_one_int_line():
    return int(read_line())


def write(case, what):
    stdout.write(f'Case #{case}: {what}\n')


def fix_slice(x, y, slice):
    """
    C?J
    J?C
    J??C
    C??J

    """

    if slice[0] == '?':
        return slice[-1] * len(slice)

    if slice[-1] == '?':
        return slice[0] * len(slice)

    if slice[0] == slice[-1]:
        return slice[0] * len(slice)

    else:

        # C?J or C??J or C???J
        # -->  CC..CJ
        # -->  CJ..JJ
        if slice[0] == C and slice[-1] == J:

            if x < y:

        return slice


def solve(x, y, w):
    print(f'x: {x}, y={y}, word={w}')
    len_w = len(w)
    if len_w == 1:
        return 0

    slices = []
    current_start = None

    for i in range(len_w):

        print(f'w[{i}] = {w[i]}')

        if w[i] == '?':
            if current_start is not None:
                print(f'nothing to do')
            else:
                current_start = i - 1
                print(f'current start: {current_start}')
        else:
            if current_start is not None:
                slices.append((current_start, i))
                current_start = None
                print(f'slices: {slices}')
                print(f'current start: {current_start}')
            else:
                print(f'nothing to do')

    if current_start is not None:
        slices.append((current_start, len_w - 1))

    end_slices = []
    for slice_i in slices:
        a, b = slice_i
        a = max(a, 0)
        slice = w[a:b + 1]
        end_slice = fix_slice(slice)
        end_slices.append(f'{slice} --> {end_slice}')

    return f'Slices: {end_slices}\n'


T = read_one_int_line()
for case in range(1, T + 1):
    x, y, word = read_line().split(' ')
    what = solve(int(x), int(y), word)
    write(case, what)
