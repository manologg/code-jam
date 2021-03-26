'''
Created on 27/04/13
Code Jam 2013 Round 1A - C
@author: manolo
'''

import sys
ifile = sys.stdin
ofile = open('./c.out', 'w')

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

