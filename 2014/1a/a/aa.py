'''
Created on 26/04/14 03:23:51 
Code Jam 2014 - 1a - a
@author: manolo
'''

import sys
ifile = sys.stdin
ofile = open('./a.out', 'w')

def r():
	return ifile.readline()[:-1]
    
def w(case, what):
	ofile.write('Case #{}: {}\n'.format(case, what))

NOT_POSSIBLE = 'NOT POSSIBLE'

def switch_outlet(outlet, pos):
	return outlet[:pos] + tuple([1-outlet[pos]]) + outlet[pos+1:]

def switch(outlets, pos, tabs):
	return [switch_outlet(o, pos) for o in outlets]

all_sw = []

def try_switch(outlets, devices, L, switches, tabs):

	if outlets == devices:
		# we found the solution
		return len(switches)
	else:
		all_sw.append(switches.copy())
		for i in range(0, L):
			switches.add(i)
			if switches not in all_sw:
				new_outlets = switch(outlets, i, tabs)
				n_switches = try_switch(set(new_outlets), set(devices), L, switches.copy(), tabs + 1)
				if n_switches is not None:
					return n_switches
				switches.remove(i)

	return None

def int_list(outlet):
	return tuple([int(char) for char in outlet])

T = int(r())
for case in range(1,T+1):

	(n, l) = r().split(' ')
	N = int(n)
	L = int(l)
	
	out = r().split(' ')
	dev = r().split(' ')

	outlets = [int_list(o) for o in out]
	devices = [int_list(d) for d in dev]
	
	all_sw = []
	n_switches = try_switch(set(outlets), set(devices), L, set(), 0)
	if n_switches is not None:
		w(case, n_switches)
	else:
		w(case, NOT_POSSIBLE)

ofile.close

