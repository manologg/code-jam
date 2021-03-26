'''
Created on 11/05/14
Code Jam 2014 - 1C - a
@author: manolo
'''

import sys
ifile = sys.stdin
ofile = open('./a.out', 'w')

def r():
    return ifile.readline()[:-1]
    
def w(case, what):
    #ofile.write('Case #{}: {}\n'.format(case, what))
    print 'Case #{}: {}\n'.format(case, what)

IMPOSSIBLE = 'impossible'

T = int(r())
for case in range(1,T+1):
    (P, Q) = r().split('/')
    p = int(P)
    q = int(Q)

    w(case, 'p={}, q={}'.format(p, q))


ofile.close

