'''
Created on 11/05/14
Code Jam 2014 - 1C - c
@author: manolo
'''

import sys
ifile = sys.stdin
ofile = open('./c.out', 'w')

def r():
    return ifile.readline()[:-1]
    
def w(case, what):
    ofile.write('Case #{}: {}\n'.format(case, what))


T = int(r())
for case in range(1,T+1):
#    (E, R, N) = r().split(' ')
#    e = int(e)
#    r = int(r)
#    n = int(N)

    w(case, what)


ofile.close

