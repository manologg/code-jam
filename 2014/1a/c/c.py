'''
Created on <DATE>
Code Jam <YEAR> <ROUND> <PROBLEM>
@author: manolo
'''

import sys
ifile = sys.stdin
ofile = open('./<PROBLEM>.out', 'w')

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

