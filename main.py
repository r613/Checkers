from create import creator
from user import Print

matrix = creator()

from moves import sall_poss
from moves import kinging
from moves import all_poss
def Input(text):
    try:    return input(text)
    except:
        print "Numbers only!"
        return Input(text)
while True:
    Print(matrix)
    cm = False
    while cm == False:
        row = Input("Row:")
        column = Input("Column:")
        lister = sall_poss(matrix,row-1,column-1,'x')
        for i in range(1,len(lister)+1):
            print i
            Print(lister[i-1])
        move = Input("Please enter the number move you would like to do (0 to try again): ")
        if move == 0:
            pass
        else:
            cm = True
    matrix = lister[move-1]
    kinging(matrix)
    Print(matrix)


    poss = all_poss(matrix,"o")
    matrix = poss[len(poss)-1]
    kinging(matrix)
    Print(matrix)
#stf =  debugger(matrix)


Print(matrix) 