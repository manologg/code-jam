'''
Created on 17/03/2013
Code Jam 2009 Qualification Round A
@author: manolo
'''

import re

def number_of_matches(pattern, words):
    #print "checking pattern " + pattern
    matches = 0
    for word in words:
        #print "'" + pattern + "' matches '" + word + "': " + str(re.match(pattern, word))
        if(re.match(pattern, word)):
            matches += 1
    return matches


import sys
i_file = sys.stdin
lines = i_file.readlines()

#for line in lines:
#    print line[:-1]

(L, D, N) = lines[0].split(' ')
word_length = int(L)
number_of_dicctionary_words = int(D)
number_of_possible_words = int(N)

existing_words = []
for i in range(1,number_of_dicctionary_words+1):
    existing_words.append(lines[i][:-1])

#print "existing words: " + str(existing_words)

result = []
possible_words = []
case = 1
for i in range(number_of_dicctionary_words+1, number_of_dicctionary_words+number_of_possible_words+1):
    word = lines[i][:-1].replace('(', '[').replace(')', ']')
    matches = number_of_matches(word, existing_words)
    #return len([word for word in words if re.match(pattern, word)])
    res = "Case #%d: %d"%(case, matches)
    case += 1
    #result.append(res)
    print res

#o_file = open('./A.out', 'w')
#o_file.writelines(result)



