'''
Created on 13/04/13
Code Jam 2013 Qualification Round C
@author: manolo
'''
from itertools import product

max_digits = 50
count = 0

for num_tuple in product('012', repeat=max_digits):
    num_str = ''.join(num_tuple)
#    print 'checking ' + str(num)
    if num == num[::-1]: # is palindrome
        num = long(num_str)
        numnum = num*num
        str_numnum = str(numnum)
        if str_numnum == str_numnum[::-1]: # is palindrome
            print num_str + ' - ' + str_numnum
            count += 1
#        else:
#            print str(numnum) + " --> NO"

print 'found: ' + str(count)

