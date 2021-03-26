'''
Created on 13/04/13
Code Jam 2013 Qualification Round C
@author: manolo
'''
import math
import sys

def is_fair(n):
    return str(n) == str(n)[::-1]

#def is_square(n):
#    sqrt = math.sqrt(n)
##    print 'sqrt = ' + str(sqrt)
#    if sqrt - long(sqrt) > 0:
#        return False
#    else:
#        return is_fair(long(sqrt))
  
 
def cond_especiales(n):
    return all(x in ['0','1','2'] for x in str(n))

def find(a, b):
    count = 0
    print '(' + str(a) + ', ' + str(b) + ')'

    sqrt_a = math.sqrt(a)
    print "sqrt_a: " + str(sqrt_a)
    long_sqrt_a = long(sqrt_a)
    print "long_sqrt_a: " + str(long_sqrt_a)
    i = long_sqrt_a
    if sqrt_a - long_sqrt_a > 0:
        i += 1
    print "i: " + str(i)

    bb = long(math.sqrt(b))
    print '(' + str(i) + ', ' + str(bb) + ')'
    while (i <= bb):
        if cond_especiales(i) and is_fair(i):
            ii = i*i
            if is_fair(ii):
                print str(i) + ' - ' + str(ii)
                count += 1
                i += 221212000L
#        else:
#            print str(i) + " --> NO"
        i +=1
    return count

a = 4000000008000000004
b = 10000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
n = find(a, b)

