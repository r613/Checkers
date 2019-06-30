def Print(matrix):
    board = ""
    board += "__________________\n"
    for row in matrix:
        row_t = ""
        for unit in row:
            if unit == 0: unit = " "
            row_t += str(unit) + " "
        board += "|" + row_t + "|\n"
    board += "------------------"
    print board
