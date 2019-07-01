def Print(matrix):
    board = ""
    #board += "__________________\n"
    
    board += "\033[4m 1,2,3,4,5,6,7,8 \033[0m\n"
    
    for row_n in range(8):
        row_t = "\033[4m"
        for unit in matrix[row_n]:
            if unit == 0: unit = " "
            row_t += str(unit) + "|"
        board += "|" + row_t + "\033[0m{}\n".format(row_n+1)
        
    board += "\033[0m"

    print board
