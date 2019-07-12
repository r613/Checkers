import os 
from create import creator
from user import Print
from ai import best
from moves import opp
from moves import sall_poss
from moves import sall_possK
from moves import sall_possM
from moves import kinging
from moves import all_poss
from moves import all_possK
from ai import game_over
from ai import bester
matrix = creator()
def Input(text):
    try:    return input(text)
    except:
        print "Numbers only!"
        return Input(text)

allmoves = []
while False:
    os.system("clear")
    for mtx in allmoves[:len(allmoves)-1]:
        Print(mtx)
    Print(matrix)
    cm = False#choice made 
    while cm == False:
        row = Input("Row:")
        column = Input("Column:")
        if all_possK(matrix,'x'):
            lister = sall_possK(matrix,row-1,column-1,'x')
        else:
            lister = sall_possM(matrix,row-1,column-1,'x')
        
        
        for i in range(1,len(lister)+1):
            print "\n\n" + str(i)
            Print(lister[i-1])

        move = Input("Please enter the number move you would like to do (0 to try again): ")
        if move == 0 or move>len(lister):
            print "Let's try again"
            pass
        else:
            cm = True
    matrix = lister[move-1]#applies the users move
    
    kinging(matrix)#King's any players who have made it to enemy border 
    allmoves.append([x[:]for x in matrix]) #saves our current position in a massive list
    #Print(matrix)#prints our current position
    poss = all_poss(matrix,"o")
    priority = [0,0,0,0,0,0,0,0,0,0,0]
    matrix = bester(poss,"o",priority)
    
    kinging(matrix)
    allmoves.append([x[:]for x in matrix])
    #Print(matrix)
#stf =  debugger(matrix)

def comparison(p1p,p2p):#if p2p is better than p2p return True
    matrix = creator()
    p1 = 0
    p2 = 0
    for rounds in range(400):
        Print(matrix)
        print p1p
        print p2p
        poss = all_poss(matrix,'x')
        matrix = bester(poss,'x',p1p)
        kinging(matrix)
        if game_over(matrix):
            break
        Print(matrix)
        print p1p
        print p2p
        poss = all_poss(matrix,'o')
        matrix = bester(poss,'o',p2p)
        kinging(matrix)
        if game_over(matrix):
            break
    if game_over(matrix) == 'x':
        p1 += 2
    elif game_over(matrix) == 'o':
        p2 += 2
    else:
        p1 += 1
        p2 += 1
    matrix = creator()
    for rounds in range(800):
        Print(matrix)
        print p1p
        print p2p
        poss = all_poss(matrix,'x')
        matrix = bester(poss,'x',p2p)
        kinging(matrix)
        if game_over(matrix):
            break
        Print(matrix)
        print p1p
        print p2p
        poss = all_poss(matrix,'o')
        matrix = bester(poss,'o',p1p)
        kinging(matrix)
        if game_over(matrix):
            break
    if game_over(matrix) == 'x':
        p2 += 2
    elif game_over(matrix) == 'o':
        p1 += 2
    else:
        p1 += 1
        p2 += 1
    return p1,p2
poss = all_poss(matrix,'x')
p1p = [0,0,0,0,5,0,0,0]
p2p = [0,0,0,0,0,0,0,0]
for i in range(0,6):
    advancing = True
    while advancing:
        p2p[i] += 1
        p1,p2 = comparison(p1p,p2p)#if p2p is better
        if p1 > p2:
            p2p = p1p[:]
            advancing = False
        elif p1 < p2:
            p1p = p2p[:]
        else:
            if p2p[i] > p1p[i] +20:
                p2p = p1p[:]
                advancing = False
            pass
Print(matrix) 