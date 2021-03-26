'''
Created on 13/04/13
Code Jam 2013 Qualification Round C
@author: manolo
'''
from itertools import product

max_digits = 50
count = 0

for num_tuple in product('012', repeat=max_digits):
    num = long(''.join(num_tuple))
#    print 'checking ' + str(num)
    if str(num) == str(num)[::-1]: # is palindrome
        numnum = num*num
        if str(numnum) == str(numnum)[::-1]: # is palindrome
            print str(num) + ' - ' + str(numnum)
            count += 1
#        else:
#            print str(numnum) + " --> NO"

print 'found: ' + str(count)

