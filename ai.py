from moves import all_poss
from moves import opp
from moves import kinging
def bester(poss,team):#returns the situation (out of the situations in poss) with the highest chances of winning (according to betterer equation)
    c = poss[0]
    for i in poss[1:]:
        if betterer(c,i,team):
            print prediction(c,team)
            print team
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
def betterer(m1,m2,team): #returns True if m1 is better than m2 according to the prediction algorithm
    if prediction(m1,team) > prediction(m2,team):
        return False
    return True
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
    allmoves = []
    runs = 0
    while game_over(temp) == False and runs < 200:
        runs += 1
        temp = best(all_poss(temp,fteam),fteam)
        kinging(temp)
        if len(allmoves)>= 4 and temp == allmoves[len(allmoves)-4]:
            return 1
        allmoves.append([x[:]for x in matrix])

        if game_over(temp):
            break

        temp = best(all_poss(temp,opp(fteam)),opp(fteam))
        kinging(temp)
        allmoves.append([x[:]for x in matrix])
        
        if len(allmoves)>= 4 and temp == allmoves[len(allmoves)-4]:
            return 1
    if runs >= 200:
        return 1
    if game_over(temp) == fteam:
        #print "won"
        return 2
    else:
        #print "lost"
        return 0

def game_over(matrix):#returns False if game isn't over, otherwise returns the (char) of the winning team 
    x = 0
    o = 0
    if all_poss(matrix,'x') == []:
        return 'o'
    elif all_poss(matrix,'o') == []:
        return 'x'
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
    score = 0
    count = 0
    
    for i in all_poss(matrix,team):
        score += win_later(i,opp(team))
        count += 1
            
    try:
        print "count: {} score: {} ".format(count,score)
        print float(score)/float(count)*100
        return float(score)/float(count)*100
    except:
        
        return float(1)
    