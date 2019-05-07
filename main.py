
def debugger(matrix):
    for row_n in range(8):
        for column_n in range(8):
            if row_n%2 == column_n%2:
                if matrix[row_n][column_n] != " ":
                    print "Error! Row: Column:  == , it has been changed back to a " "".format(row_n,column_n,matrix[row_n][column_n])
            else:

                matrix[row_n][column_n] = "0"
    return matrix
matrix = [[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]]
stf =  debugger(matrix)

def Print(matrix):
    board = ""
    board += "__________________\n"
    for row in matrix:
        row_t = ""
        for unit in row:
            row_t += unit 
            row_t += " "
        board += "|" + row_t + "|\n"
    
    board += "------------------"
    print board 
Print(stf) 