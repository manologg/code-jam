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

ofile = open('./c-large1-2.out', 'w')
def w(what):
    ofile.write(what + '\n')


nnn = [1, 4, 9, 121, 484, 10201, 12321, 14641, 40804, 44944, 1002001, 1234321, 4008004, 100020001, 102030201, 104060401, 121242121, 123454321, 125686521, 400080004, 404090404, 10000200001, 10221412201, 12102420121, 12345654321, 40000800004, 1000002000001, 1002003002001, 1004006004001, 1020304030201, 1022325232201, 1024348434201, 1210024200121, 1212225222121, 1214428244121, 1232346432321, 1234567654321, 4000008000004, 4004009004004]


def find(a, b):
    my_set = [x for x in nnn if x >= a and x <= b]
    return len(my_set)

t = long(r())
#print 't: ' + str(t)

for i in xrange(t):
    (A, B) = r().split(' ')
    a = long(A)
    b = long(B)
    n = find(a, b)
    w('Case #' + str(i+1) + ': ' + str(n))

ofile.close

