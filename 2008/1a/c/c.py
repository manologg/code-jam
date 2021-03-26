'''
Created on 12/04/13
Code Jam 2008 Round 1A C
@author: manolo
'''

ofile = open('./c-small.out', 'w')

def w(what):
    ofile.write(what + '\n')

from decimal import *
getcontext().prec = 100
base = 3 + Decimal(5)**Decimal('0.5')
def calc(n):
    return Decimal(base)**Decimal(n)

import sys
ifile = sys.stdin

nc = int(ifile.readline())
print 'nc: ' + str(nc)

for i in range(nc):
    n = int(ifile.readline())
    num = calc(n)
    num2 = int(num % 1000)
    lennum = len(str(num2))
    if lennum < 3:
        nzeros = 3 - lennum
        w('Case #' + str(i+1) + ': ' + ('0'* nzeros) + str(num2))
    else:
        w('Case #' + str(i+1) + ': ' + str(num2))

ofile.close

