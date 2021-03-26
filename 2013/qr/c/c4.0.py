'''
Created on 13/04/13
Code Jam 2013 Qualification Round C
@author: manolo
'''
from itertools import product

max_digits = 50
possible = ['0', '1', '2']
#    0**(len(str(a))+1) + a*10 + 1

#numbers = []

ofile = open('./c-numbers_10_' + str(max_digits) + '_0', 'w')
def w(what):
    ofile.write(what + '\n')

def check_number(num):
    numnum = num*num
    str_numnum = str(numnum)
    if str_numnum == str_numnum[::-1]: # is palindrome
        w(str(num) + ' - ' + str_numnum)
#    else:
#        print str(numnum) + " --> NO"

def gen_pals(base):
    if base[0] != '0' and len(base) <= max_digits:
#        numbers.append(int(base))
        check_number(int(base))
#    print base
    if len(base) < max_digits:
        for n in possible:
            new_base = n + base + n
            gen_pals(new_base)

gen_pals('0')

#print numbers
#print '...'
#print sorted(numbers)
    

