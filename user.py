def Print(matrix):
    board = ""
    #board += "__________________\n"
    
    board += "|1|2|3|4|5|6|7|8| \n"
    
    for row_n in range(8):
        row_t = ""
        for unit in matrix[row_n]:
            if unit == 0: unit = " "
            row_t += str(unit) + " "
        board += "|" + row_t + "|{}\n".format(row_n+1)
    board += "------------------"

    print board
