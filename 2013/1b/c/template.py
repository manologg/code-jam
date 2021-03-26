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
    
def w(what):
    ofile.write(what + '\n')


T = int(r())
for case in range(1,T+1):
#    (E, R, N) = r().split(' ')
#    e = int(e)
#    r = int(r)
#    n = int(N)

    w('Case #' + str(case) + ': ' + )


ofile.close

