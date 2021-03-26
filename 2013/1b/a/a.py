'''
Created on 04/05/13 
Code Jam 2013 - Round 1B - A
@author: manolo
'''

import sys
ifile = sys.stdin
ofile = open('./a-small.out', 'w')

def r():
    return ifile.readline()[:-1]
    
def w(what):
    ofile.write(what + '\n')

def careful(armin, n_moles):
    plus_1 = 0
    i = 0
    while i < len(motes):
        mote = motes[i]
        if armin > mote:
            print 'absorb: ' + str(mote)
            armin += mote
            i += 1
        else:
            print 'can\'t absorb it: ' + str(mote)
            if plus_1 < (n_moles - i):
                print 'put one more: ' + str(armin-1)
                armin += armin - 1
                plus_1 += 1
            else:
                break
        print '         armin: ' + str(armin)
    left = n_moles - i
    
    print 'careful: ' + str(plus_1) + '+' + str(left)
    
    return plus_1 + left

def eager(armin, n_moles):
    plus_1 = 0
    i = 0
    while i < len(motes):
        mote = motes[i]
        if armin > mote:
            print 'absorb: ' + str(mote)
            armin += mote
            i += 1
        else:
            print 'can\'t absorb it: ' + str(mote)
            print 'put one more: ' + str(armin-1)
            armin += armin - 1
            plus_1 += 1
        print '         armin: ' + str(armin)
    
    print 'eager: ' + str(plus_1)
    
    return plus_1

T = int(r())
for case in range(1,T+1):
    (a, n_moles) = [int(x) for x in r().split(' ')]
    motes = [int(x) for x in r().split(' ')]
    motes.sort()
    print 'case #' + str(case)
    print 'armin: ' + str(a)
    print 'motes: ' + str(motes)
    
    if a == 1:
        print 'result: n_moles: ' + str(n_moles)
        w('Case #' + str(case) + ': ' + str(n_moles))
        print '_______________________________________________________________\n'
        continue

    result_careful = careful(a, n_moles)
    print '---------------'
    result_eager = eager(a, n_moles)
    print '---------------'
    print 'n_moles: ' + str(n_moles)

    w('Case #' + str(case) + ': ' + str(min(result_careful, n_moles)))
    print '_______________________________________________________________\n'


ofile.close

