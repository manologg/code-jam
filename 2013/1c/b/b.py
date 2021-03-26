'''
Created on 12/05/2013
Code Jam 2013 1C - B
@author: manolo
'''

import sys
ifile = sys.stdin
ofile = open('./b.out', 'w')

def r():
    return ifile.readline()[:-1]
    
def w(what):
    sys.stdout.write(what + '\n')
    ofile.write(what + '\n')

def get_to(x0, y0, x, y, incr, jumps, d):


    print '  ' * d + 'we\'re in (' + str(x0) + ',' + str(y0) + ') and we want to get to (' + str(x) + ',' + str(y) + ') we jump now', incr

    if (x0, y0) == (x, y):
        print '  ' * d + 'we\'re already there!'
        return (True, jumps)
    
    find = False
    
    curr_incr = incr + 1
        
    # north (increasing y)
    if abs(y0+curr_incr-y) < abs(y0-y):
        
        print '  ' * d + 'go North', curr_incr, 'steps'
            
        (find, jumps) = get_to(x0, y0+curr_incr, x, y, curr_incr, jumps+'N', d+1)
        
        if find:
            return (find, jumps)
        else:
            print '  ' * d + 'not found, continue searching'
    
    
    # south (decreasing y)
    if abs(y0-curr_incr-y) < abs(y0-y):

        print '  ' * d + 'go South', curr_incr, 'steps'
    
        (find, jumps) = get_to(x0, y0-curr_incr, x, y, curr_incr, jumps+'S', d+1)
    
        if find:
            return (find, jumps)
        else:
            print '  ' * d + 'not found, continue searching'
    
    
    # east (increasing x)
    if abs(x0+curr_incr-x) < abs(x0-x):
  
        print '  ' * d + 'go East', curr_incr, 'steps'
        
        (find, jumps) = get_to(x0+curr_incr, y0, x, y, curr_incr, jumps+'E', d+1)
      
        if find:
            return (find, jumps)
        else:
            print '  ' * d + 'not found, continue searching'
    
    
    # west (decreasing x)
    if abs(x0-curr_incr-x) < abs(x0-x):
    
        print '  ' * d + 'go West', curr_incr, 'steps'
        
        (find, jumps) = get_to(x0-curr_incr, y0, x, y, curr_incr, jumps+'W', d+1)
      
        if find:
            return (find, jumps)
        else:
            print '  ' * d + 'not found, continue searching'


    return (find, jumps)

T = int(r())
for case in range(1,T+1):
    (x, y) = [int(c) for c in r().split(' ')]
    print x, y
    
    (find, jumps) = get_to(0, 0, x, y, 0, '', 0)
    
    if not find:
        print 'PATH NOT FIND!!!'
    
    w('Case #' + str(case) + ': ' + str(jumps))
    print '______________________________\n'



ofile.close

