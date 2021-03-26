'''
Created on 13/04/13
Code Jam 2013 Qualification Round C
@author: manolo
'''
import math
import sys
ifile = sys.stdin
def r():
    return ifile.readline()[:-1]

ofile = open('./c-example.out', 'w')
def w(what):
    ofile.write(what + '\n')

def is_fair(n):
    return str(n) == str(n)[::-1]

def is_square(n):
    sqrt = math.sqrt(n)
#    print 'sqrt = ' + str(sqrt)
    if sqrt - long(sqrt) > 0:
        return False
    else:
        return is_fair(long(sqrt))
    

def find(a, b_):
    count = 0
    b = long(b_+1)
    print '(' + str(a) + ', ' + str(b) + ')'
    i = a
    while (i <= b):
        if is_fair(i) and is_square(i):
            print i
            count += 1
#        else:
#            print str(i) + " --> NO"
        i +=1
    return count

t = long(r())
print 't: ' + str(t)

for i in xrange(t):
    (A, B) = r().split(' ')
    a = long(A)
    b = long(B)
    n = find(a, b)
    w('Case #' + str(i+1) + ': ' + str(n))

ofile.close

