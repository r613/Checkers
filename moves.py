from user import Print
def all_poss(matrix,team):#returns all possible outcomes for this position on the board
    poss = []
    for r in range(8):
        for c in range(8):
            if r%2 == c%2: #if it's from the black spaces on the board 
                if str(matrix[r][c]).lower() == team : #if there is a piece on 
                    poss += sall_poss(matrix,r,c,team)
    return poss
def sall_poss(m,r,c,team):#returns a list of all possible (legal) moves that could be done from our location (ONLY if the unit in this space is on our team)
    nlist = []
    if team == "x":
        if m[r][c] == team: #our piece is lowercase, therefor can only move forward
            #lister contains ALL the moves can be done from our location #at least of them should be False (moves that couldn't have been done)
            lister = [u_moveL(m,r,c),   u_moveR(m,r,c), u_moveLKill(m,r,c), u_moveRKill(m,r,c)]
            for i in lister:
                if i:
                    nlist.append(i)
            #nlist includes all the possible moves from our location 
        
        elif str(m[r][c]).lower() == team:
            #lister contains ALL the moves can be done from our location #at least of them should be False (moves that couldn't have been done)
            lister = [u_moveL(m,r,c),   u_moveR(m,r,c), d_moveL(m,r,c), d_moveR(m,r,c), u_moveLKill(m,r,c), u_moveRKill(m,r,c), d_moveLKill(m,r,c), d_moveRKill(m,r,c)]
            for i in lister:
                if i:
                    nlist.append(i)
    if team == "o":
        if m[r][c] == team:
        
            #lister contains ALL the moves can be done from our location #at least of them should be False (moves that couldn't have been done)
            lister = [d_moveL(m,r,c), d_moveR(m,r,c),d_moveLKill(m,r,c), d_moveRKill(m,r,c)]
            for i in lister:
                if i:
                    nlist.append(i)
            #nlist includes all the possible moves from our location 
        
        elif str(m[r][c]).lower() == team:
        
            #lister contains ALL the moves can be done from our location #at least of them should be False (moves that couldn't have been done)
            lister = [u_moveL(m,r,c),   u_moveR(m,r,c), d_moveL(m,r,c), d_moveR(m,r,c), u_moveLKill(m,r,c), u_moveRKill(m,r,c), d_moveLKill(m,r,c), d_moveRKill(m,r,c)]
            for i in lister:
                if i:
                    nlist.append(i)
    
    return nlist
def opp(team):#know your enemy
    if team.lower() == 'x':
        return 'o'
    else:
        return 'x'
    
def u_moveL(matrix,r,c):
    if r > 0 and c > 0:#we can move it
        if matrix[r-1][c-1] == 0:
            temp = [x[:]for x in matrix]
            temp[r-1][c-1] = temp[r][c]
            temp[r][c] = 0
            return temp
    return False
def u_moveLKill(matrix,r,c):
    team = matrix[r][c].lower()
    if r > 1 and c > 1:#we can jump in this direction (+2)
        if str(matrix[r-1][c-1]).lower() == opp(team): #if the space we are looking at isn't on the same team as our current space
            if matrix[r-2][c-2] == 0:#empty - so we can land on it
                temp = [x[:]for x in matrix]
                temp[r-2][c-2] = temp[r][c]
                temp[r-1][c-1] = 0
                temp[r][c] = 0
                return temp
    return False
def u_moveR(matrix,r,c):
    if r > 0 and c < 7:#we can move in this direction
        if matrix[r-1][c+1] == 0:#the landing space is empty
            temp = [x[:]for x in matrix]
            temp[r-1][c+1] = temp[r][c]
            temp[r][c] = 0
            return temp
    return False
def u_moveRKill(matrix,r,c):
    team = matrix[r][c].lower()
    
    if r > 1 and c < 6:
        if str(matrix[r-1][c+1]).lower() == opp(team):
            if matrix[r-2][c+2] == 0:
                temp = [x[:]for x in matrix]
                temp[r-2][c+2] = temp[r][c]
                temp[r-1][c+1] = 0
                temp[r][c] = 0
                return temp
    return False

def d_moveR(matrix,r,c):
    if r < 7 and c < 7:#we can move in this direction
        if matrix[r+1][c+1] == 0:#the landing space is empty
            temp = [x[:]for x in matrix]
            temp[r+1][c+1] = temp[r][c]
            temp[r][c] = 0
            return temp
    return False
def d_moveRKill(matrix,r,c):
    team = matrix[r][c].lower()
    if r < 6 and c < 6:#we can jump in this direction (+2)
        if str(matrix[r+1][c+1]).lower() == opp(team): #if the space we have here isn't on our team (also not cap of out team) 
            if matrix[r+2][c+2] == 0:#empty - so we can land on it
                temp = [x[:]for x in matrix]
                temp[r+2][c+2] = temp[r][c]
                temp[r+1][c+1] = 0
                temp[r][c] = 0
                return temp
    return False
def d_moveL(matrix,r,c):
    if r < 7 and c > 0:#we can move it
        if matrix[r+1][c-1] == 0:
            temp = [x[:]for x in matrix]
            temp[r+1][c-1] = temp[r][c]
            temp[r][c] = 0
            return temp
    return False
def d_moveLKill(matrix,r,c):
    team = matrix[r][c].lower()
    if r < 6 and c > 1:#we can jump in this direction (+2)
        if str(matrix[r+1][c-1]).lower() == opp(team): #if the space we have here isn't on our team (also not cap of out team) 
            if matrix[r+2][c-2] == 0:#empty - so we can land on it
                temp = [x[:]for x in matrix]
                temp[r+2][c-2] = temp[r][c]
                temp[r+1][c-1] = 0
                temp[r][c] = 0
                return temp
    return False

def kinging(matrix):
    for column in range(8):
        if matrix[0][column] == "x":
            matrix[0][column] = "X"
    for column in range(8):
        if matrix[7][column] == "o":
            matrix[7][column] = "O"