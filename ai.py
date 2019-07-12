from moves import all_poss
from moves import opp
from moves import kinging
from moves import all_possK
def bester(poss,team,priority):#returns the situation (out of the situations in poss) with the highest chances of winning (according to betterer equation)
    c = poss[0]
    for i in poss[1:]:
        if betterer(c,i,team,priority):
            #print prediction(c,team,priority)
            #print team
            c = i
    return c

def best(poss,team,priority):
    if poss == []:
        return False
    
    c = poss[0]
    for i in poss[1:]:
        if better(c,i,team,priority):
            c = i
    return c
def betterer(m1,m2,team,priority): #returns True if m1 is better than m2 according to the prediction algorithm
    if prediction(m1,team,priority) > prediction(m2,team,priority):
        return False
    return True

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

def win_later(matrix,fteam,priority):#The computer plays against itself (using the basic algorithm of best) and returns if fteam wins 
    temp = [x[:]for x in matrix]
    allmoves = []
    runs = 0
    while game_over(temp) == False and runs < 200:
        runs += 1
        temp = best(all_poss(temp,fteam),fteam,priority)
        kinging(temp)
        if len(allmoves)>= 4 and temp == allmoves[len(allmoves)-4]:
            return 1
        allmoves.append([x[:]for x in matrix])

        if game_over(temp):
            break

        temp = best(all_poss(temp,opp(fteam)),opp(fteam),priority)
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
        print 'x'
        return 'x'
    elif o == 0:
        print 'o'
        return 'o'
    return False
def prediction(matrix,team,priority):
    score = 0
    count = 0
    
    for i in all_poss(matrix,team):
        score += win_later(i,opp(team),priority)
        count += 1
            
    try:
        #print "count: {} score: {} ".format(count,score)
        #print float(score)/float(count)*100
        return float(score)/float(count)*100
    except:
        
        return float(1)

#counts pices at sides 
#counts pieces at back line 
def better(m1,m2,team,priority):
    m1p = 0
    m2p = 0
    #0-enemy king count 1-enemy piece count
    
    m1p += king_count(m1,opp(team))*(-priority[0])
    m2p += king_count(m1,opp(team))*(-priority[0])
    
    m1p += piece_count(m1,opp(team))*(-priority[1])
    m2p += piece_count(m2,opp(team))*(-priority[1])
    
    #2-sidepiece count 3-enemy sidepiece count
    m1p += side_count(m1,team)*priority[2]
    m2p += side_count(m2,team)*priority[2]

    m1p += side_count(m1,opp(team))*(-priority[3])
    m2p += side_count(m2,opp(team))*(-priority[3])

    m1p += enemy_kills(m1,team) * (-priority[4])
    m2p += enemy_kills(m2,team) * (-priority[4])
    if m1p < m2p:
        return True
    else:
        return False
def enemy_kills(matrix,team):
    num = len(all_possK(matrix,opp(team)))

    return num

def side_count(matrix,team):
    return 0