from moves import all_poss
from moves import opp
from moves import kinging
def betterer(m1,m2,team): #returns True if m1 is better than m2 according to the prediction algorithm
    if prediction(m1,team) > prediction(m2,team):
        return False
    return True
def bester(poss,team):#returns the situation (out of the situations in poss) with the highest chances of winning (according to betterer equation)
    c = poss[0]
    for i in poss[1:]:
        if betterer(c,i,team):
            print prediction(c,team)
            c = i
    return c

def best(poss,team):
    if poss == []:
        return False
    
    c = poss[0]
    for i in poss[1:]:
        if better(c,i,team):
            c = i
    return c
def better(m1,m2,team):
    count1 = king_count(m1,opp(team))
    count2 = king_count(m2,opp(team))   
    if count1<count2:
        return False
    elif count1>count2:
        return True
    else:
        count1 = piece_count(m1,opp(team))
        count2 = piece_count(m2,opp(team))
        if count1<count2:
            return False
        elif count1>count2:
            return True
        else:
            return False
def king_count(matrix,team):
    count = 0
    for i in range(8):
        for j in range(8):
            if matrix[i][j] == team:
                count += 1
    return count

def piece_count(matrix,team):
    count = 0
    for i in range(8):
        for j in range(8):
            if str(matrix[i][j]).lower() == team:
                count += 1
    return count 

def win_later(matrix,fteam):#The computer plays against itself (using the basic algorithm of best) and returns if fteam wins 
    temp = [x[:]for x in matrix]
    while game_over(temp) == False:
        temp = best(all_poss(temp,fteam),fteam)
        kinging(temp)
        if game_over(temp):
            break
        temp = best(all_poss(temp,opp(fteam)),opp(fteam))
        kinging(temp)
    if game_over(temp) == fteam:
        #print "won"
        return True
    else:
        #print "lost"
        return False

def game_over(matrix):#returns False if game isn't over, otherwise returns the (char) of the winning team 
    x = 0
    o = 0
    for row in matrix:
        for unit in row:
            if str(unit).lower() == 'x':
                x += 1
            elif str(unit).lower() == 'o':
                o += 1
            else:
                pass
    if x == 0:
        return 'x'
    elif o == 0:
        return 'o'
    return False
def prediction(matrix,team):
    win = 0
    los = 0
    for i in all_poss(matrix,team):
        if win_later(i,opp(team)):
            los += 1
        else:
            win += 1
    try:
        print float(win)/float(los)
        print "yes"
        return float(win)/float(los)
    except:
        print 'weird but returning '
        return float(0.00001)
    