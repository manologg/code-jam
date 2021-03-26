'''
Created on 27/04/13
Code Jam 2013 Round 1A - A
@author: manolo
'''

import sys
from itertools import count
ifile = sys.stdin
ofile = open('./a-large.out', 'w')

def read():
    return ifile.readline()[:-1]
    
def w(what):
#    print what
    ofile.write(what + '\n')

T = int(read())
#print str(T) + ' cases'
for i in range(1,T+1):
    (r, t) = read().split(' ')
    r = int(r)
    t = int(t)
#    print 'r = ' + str(r)
#    print 't = ' + str(t)
    
    n_circles = 1
    
    for radio in count(start=r+1, step=2):
        milimeters = 2 * radio - 1
#        print 'radio: ' + str(radio)
#        print 'milimeters: ' + str(milimeters)
        t = t - milimeters
#        print 't: ' + str(t)
        if(t < 0):
            w('Case #' + str(i) + ': ' + str(n_circles-1))
            break
        n_circles += 1

#    sys.stdout.write('.')
    




ofile.close

