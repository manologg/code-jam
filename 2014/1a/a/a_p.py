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
	#print 'Case #{}: {}\n'.format(case, what)

NOT_POSSIBLE = 'NOT POSSIBLE'

def switch_outlet(outlet, pos):
	return outlet[:pos] + tuple([1-outlet[pos]]) + outlet[pos+1:]

def switch(outlets, pos, tabs):
	print '\t' * tabs + 'switching in position {}'.format(pos)
	return [switch_outlet(o, pos) for o in outlets]

all_sw = []

def try_switch(outlets, devices, L, switches, tabs):

	print '\t' * tabs + '......'
	print '\t' * tabs + 'checking outlets and devices with switches: {}'.format(switches)
	print '\t' * tabs + 'outlets: {}'.format(outlets)
	print '\t' * tabs + 'devices: {}'.format(devices)
	print '\t' * tabs + 'equals? {}'.format(outlets == devices)

	if outlets == devices:
		# we found the solution
		return len(switches)
	else:
		all_sw.append(switches.copy())
		print '\t' * tabs + 'all_sw: {}'.format(all_sw)
		for i in range(0, L):
			switches.add(i)
			print '\t' * tabs + '--> {}'.format(i)
			print '\t' * tabs + 'switches: {}'.format(switches)
			print '\t' * tabs + 'all_sw: {}'.format(all_sw)
			print '\t' * tabs + 'switches in all_sw: {}'.format(switches in all_sw)
			if switches not in all_sw:
				print '\t' * tabs + 'before: {}'.format(outlets)
				new_outlets = switch(outlets, i, tabs)
				print '\t' * tabs + 'after: {}'.format(new_outlets)
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
	
	print "{} outlets with lenght {}: {}".format(N, L, outlets)
	print "{} devices with lenght {}: {}".format(N, L, devices)

	all_sw = []
	n_switches = try_switch(set(outlets), set(devices), L, set(), 0)
	if n_switches is not None:
		w(case, n_switches)
	else:
		w(case, NOT_POSSIBLE)

	print "----------------"


ofile.close

