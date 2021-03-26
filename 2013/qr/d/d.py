'''
Created on 13/04/13
Code Jam 2013 Qualification Round D
@author: manolo
'''

import sys
ifile = sys.stdin
def r():
    return ifile.readline()[:-1]

ofile = open('./d.out', 'w')
def w(what):
    ofile.write(what + '\n')


t = int(r())
print 't: ' + str(t)

for i in range(t):

(L, D, N) = r().split(' ')
l = int(L)
d = int(D)
n = int(N)

w('Case #1: ')


ofile.close

