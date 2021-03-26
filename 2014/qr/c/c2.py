'''
Created on 12/04/14 
Code Jam 2014 QR C
@author: manolo
'''

import sys
ifile = sys.stdin
ofile = open('./c.out', 'w')

def read():
    return ifile.readline()[:-1]
    
def w_case(case):
    ofile.write('Case #{}:\n'.format(case))

def w_what(what):
#    ofile.write('{}\n'.format(what))
    print '{}\n'.format(what)

impossible = 'Impossible'

T = int(read())
for case in range(1,T+1):
    (R, C, M) = read().split(' ')
    r = int(R)
    c = int(C)
    m = int(M)

    print 'board: {}x{} with {} mines'.format(r, c, m)
    board = [[None] * c] * r
    w_case(case)
    
    reverse = False
    
    if r < c:
        reverse = True
        r,c = c,r
    
    # I ASSUME THAT r >= c (if not, we reverse it later)
    
    # c = 1, r = [2,n] (c = 1, r = 1 makes no sense)
    if c == 1:
        for i in range(m):
            board[i][0] = '*'
        for i in range(m, r - 1):
            board[i][0] = '.'
        board[r-1][0] = 'c'
    
    # c = 2, r = 2
    elif c == 2 and r == 2:
        if m == 0:
            board = w_what('..\n.c')
        elif m == 1:
            w_what(impossible)
        elif m == 2:
            w_what(impossible)
        elif m == 3:
            board = w_what('**\n*c')

    # r >= c, r > 2, c > 2
    else:
        pass
#        mines_r = m / c  # rows with mines
#        
#        print "mines_r : {}".format(mines_r)
#        
#        for i in range(mines_r):
#            board[i] = '*' * c
#        
#        rest_r = r - mines_r # rest of the rows
#        rest_m = m % c  # rest of the mines to put
#        
#        print "rest_r : {}".format(rest_r)
#        print "rest_m : {}".format(rest_m)
#        
#        # I took all lines with mines away and there are no more mines to put
#        if rest_m == 0:
#        
#            # there's just one row left --> we can NOT win in 1 click
#            if rest_r == 1:
#                w_what(impossible)
#                
#            # there are more than one row --> we can win in 1 click
#            else:
#                for i in range(mines_r, r-1):
#                    board[i] = '.' * c
#                for i in range(c-1):
#                    board[r-1][i] = '.'
#                board[r-1][c-1] = 'c'
#                
#        # there are some mines to put
#        else:
#        
#            # there's just one row left
#            if rest_r == 1:
#            
#                # we have just one possible click --> we can win in 1 click
#                if rest_m == c - 1:
#                    for i in range(c-1):
#                        board[r-1][i] = '*'
#                    board[r-1][c-1] = 'c'
#                
#                # we have multiple clicks --> we can NOT win in 1 click
#                else:
#                    w_what(impossible)
#                
#            # there are 2 rows left
#            elif rest_r == 2:
#            
#                # we have to put 1 or 2 mines more --> we can win in 1 click
#                if rest_m == 1 or rest_m == 2:
#                   
#                    # row with mines and dots
#                    for i in range(rest_m):
#                        board[mines_r][i] = '*'
#                    for i in range(rest_m, c):
#                        board[mines_r][i] = '.'
#                        
#                    # row with one dot, click and more dots
#                    board[mines_r + 1][0] = '.'
#                    board[mines_r + 1][1] = 'c'
#                    for i in range(2, c):
#                        board[mines_r + 1][i] = '.'
#            
#                # we have to put more than 2 mines --> we can NOT win in 1 click
#                else:
#                    w_what(impossible)
#                
#            
#            # there are more than 2 rows left
#            else:
#                
#                # row with mines and dots
#                for i in range(rest_m):
#                    board[mines_r][i] = '*'
#                for i in range(rest_m, c):
#                    board[mines_r][i] = '.'
#                
#                # row with dots, click and more dots
#                for i in range(rest_m - 1):
#                    board[mines_r + 1][i] = '.'
#                board[mines_r + 1][rest_m - 1] = 'c'
#                for i in range(rest_m, c):
#                    board[mines_r + 1][i] = '.'
#                
#                # rest of the rows (just dots)
#                for i in range(mines_r + 2, r):
#                    board[i] = '.' * c
                
    if reverse:
        board = zip(*board)
        
    for row in board:
        print row
        
ofile.close

































