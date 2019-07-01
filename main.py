import os 
from create import creator
from user import Print
from ai import best
matrix = creator()
from moves import opp
from moves import sall_poss
from moves import kinging
from moves import all_poss
from ai import bester
def Input(text):
    try:    return input(text)
    except:
        print "Numbers only!"
        return Input(text)

allmoves = []
while True:
    Print(matrix)
    cm = False#choice made 
    while cm == False:
        row = Input("Row:")
        column = Input("Column:")
        lister = sall_poss(matrix,row-1,column-1,'x')#list of all possible moves from our unit
        for i in range(1,len(lister)+1):
            print "\n\n" + str(i)
            Print(lister[i-1])

        move = Input("Please enter the number move you would like to do (0 to try again): ")
        if move == 0 or move>len(lister):
            print "Let's try again"
            pass
        else:
            cm = True
    matrix = lister[move-1]#makes the users move
    
    kinging(matrix)#King's any players who have made it to enemy border 
    allmoves.append([x[:]for x in matrix]) #saves our current position in a massive list
    os.system("clear")
    for mtx in allmoves:
        Print(mtx)
    #Print(matrix)#prints our current position
    
    poss = all_poss(matrix,"o")
    matrix = bester(poss,"o")
    
    kinging(matrix)
    allmoves.append([x[:]for x in matrix])
    #Print(matrix)
#stf =  debugger(matrix)


Print(matrix) 