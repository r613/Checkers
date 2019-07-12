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
            
            lister = [u_moveL(m,r,c),   u_moveR(m,r,c), d_moveL(m,r,c), d_moveR(m,r,c), u_moveLKill(m,r,c), u_moveRKill(m,r,c), d_moveLKill(m,r,c), d_moveRKill(m,r,c)]
            for i in lister:
                if i:
                    nlist.append(i)
    if team == "o":
        if m[r][c] == team:
        
            
            lister = [d_moveL(m,r,c), d_moveR(m,r,c),d_moveLKill(m,r,c), d_moveRKill(m,r,c)]
            for i in lister:
                if i:
                    nlist.append(i)
            
        
        elif str(m[r][c]).lower() == team:
        
            
            lister = [u_moveL(m,r,c),   u_moveR(m,r,c), d_moveL(m,r,c), d_moveR(m,r,c), u_moveLKill(m,r,c), u_moveRKill(m,r,c), d_moveLKill(m,r,c), d_moveRKill(m,r,c)]
            for i in lister:
                if i:
                    nlist.append(i)
    
    return nlist





def sall_possK(m,r,c,team):#returns a list of all possible (legal) moves that could be done from our location (ONLY if the unit in this space is on our team)
    nlist = []
    if team == "x":
        if m[r][c] == team: #our piece is lowercase, therefor can only move forward
            #lister contains ALL the moves can be done from our location #at least of them should be False (moves that couldn't have been done)
            lister = [u_moveLKill(m,r,c), u_moveRKill(m,r,c)]
            for i in lister:
                if i:
                    nlist.append(i)
            #nlist includes all the possible moves from our location 
        
        elif str(m[r][c]).lower() == team:
            
            lister = [u_moveLKill(m,r,c), u_moveRKill(m,r,c), d_moveLKill(m,r,c), d_moveRKill(m,r,c)]
            for i in lister:
                if i:
                    nlist.append(i)
    if team == "o":
        if m[r][c] == team:
        
            
            lister = [d_moveLKill(m,r,c), d_moveRKill(m,r,c)]
            for i in lister:
                if i:
                    nlist.append(i)
            
        
        elif str(m[r][c]).lower() == team:
        
            
            lister = [u_moveLKill(m,r,c), u_moveRKill(m,r,c), d_moveLKill(m,r,c), d_moveRKill(m,r,c)]
            for i in lister:
                if i:
                    nlist.append(i)
    
    return nlist
def sall_possm(m,r,c,team):#returns a list of all possible (legal) moves that could be done from our location (ONLY if the unit in this space is on our team)
    nlist = []
    if team == "x":
        if m[r][c] == team: #our piece is lowercase, therefor can only move forward
            #lister contains ALL the moves can be done from our location #at least of them should be False (moves that couldn't have been done)
            lister = [u_moveL(m,r,c),   u_moveR(m,r,c)]
            for i in lister:
                if i:
                    nlist.append(i)
            #nlist includes all the possible moves from our location 
        
        elif str(m[r][c]).lower() == team:
            
            lister = [u_moveL(m,r,c),   u_moveR(m,r,c), d_moveL(m,r,c), d_moveR(m,r,c)]
            for i in lister:
                if i:
                    nlist.append(i)
    if team == "o":
        if m[r][c] == team:
        
            
            lister = [d_moveL(m,r,c), d_moveR(m,r,c)]
            for i in lister:
                if i:
                    nlist.append(i)
            
        
        elif str(m[r][c]).lower() == team:
        
            
            lister = [u_moveL(m,r,c),   u_moveR(m,r,c), d_moveL(m,r,c), d_moveR(m,r,c)]
            for i in lister:
                if i:
                    nlist.append(i)
    
    return nlist