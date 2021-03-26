'''
Created on 27/04/13
Code Jam 2013 Round 1A - B
@author: manolo
'''

import sys
ifile = sys.stdin
ofile = open('./b-small.out', 'w')

def r():
    return ifile.readline()[:-1]
    
def w(what):
#    print what
    ofile.write(what + '\n')


T = int(r())
for case in range(1,T+1):
    (E, G, N) = r().split(' ')
    max_e = int(E)
#    print "max_e: " + str(max_e)
    g = int(G)
#    print "regain: " + str(g)
    n = int(N)
    e = max_e
    gain = 0
    vs_str = r().split(' ')
    vs = [int(x) for x in vs_str]
#    print "vs: " + str(vs)
    max_v = max(vs)
#    print "max_v: " + str(max_v)
    for v in vs:
#        print "v: " + str(v)
        if len(vs) == 1:
            used_e = e
        elif v == max_v:
            used_e = e
        elif g >= e:
            used_e = e
#            print "a tope!!! used_e: " + str(used_e)
        else:
            v_ = v/float(max_v)
#            print "v_: " + str(v_)
            used_e = int(v_ * e)
            if used_e > e:
                used_e = e
#            print "used_e: " + str(used_e)
            
        gain += v * used_e
#        print "gain: " + str(gain)
        
        e = e - used_e + g
        if e > max_e:
            e = max_e
        
#        print "e: " + str(e)
        
    w('Case #' + str(case) + ': ' + str(gain))
#    print "----------------"


ofile.close

