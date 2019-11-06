import string
string_case=list(string.ascii_uppercase)
def string_integer(y):
    return (string_case.index(y)+1)

def coordinate_positions(coordinate):
    x,y=coordinate[0],coordinate[1]
    x=string_integer(x)
    y=int(y)
    return x,y

def position_coordinate(coordinate):
    x,y=coordinate
    x=string_case[x]
    return x+str(y)
    

def ship_positions(coordinate,width,height,type_ship):
    a=[]
    x,y=coordinate_positions(coordinate)
    for i in range(width):
        for j in range(height):
            calc=x+j,y+i
            a.append(calc)
    if type_ship=='Q':
        return a*2
    else:
        return a

dimensions=raw_input()
x,y=dimensions.split(" ")
y=string_integer(y)
x=int(x)
y=int(y)
player1=[]
player2=[]
total_ships=input()
for twice in range(2):
    type1=raw_input().split(" ")
    x1,y1=int(type1[1]),int(type1[2])
    even=0
    for i in type1[3:]:
        if even%2==0:
            player1_ships=ship_positions(i,x1,y1,type1[0])
            for i in player1_ships:
                player1.append(i)
        else:
            player2_ships=ship_positions(i,x1,y1,type1[0])
            for i in player2_ships:
                player2.append(i)
        even+=1
missile_player1=[]
missile1=raw_input().split(" ")
for i in missile1:
    a=coordinate_positions(i)
    missile_player1.append(a)
missile_player2=[]
missile2=raw_input().split(" ")
for i in missile2:
    a=coordinate_positions(i)
    missile_player2.append(a)
    
def attack_player2(flag=0):
    if len(missile_player2)==0:
        print "Player 2 has no missiles"
        flag_player2=1
        if flag==1:
            if len(player1)!=0 or len(player2)!=0:
                print("Peace")
                exit()
        else:
            attack_player1(flag_player2)
    else:
        m2=[]
        for m in missile_player2:
            m2.append(m)
        for i in m2:
            if i in player1:
                x=position_coordinate(i)
                print "Player 2 fires a missile with target "+x+" which got HIT"
                player1.remove(i)
                if len(player1)==0:
                    print("Player2 Won")
                    exit()
                del missile_player2[0]
                attack_player2()
            else:
                x=position_coordinate(i)
                print "Player-2 fires a missile with target "+x+" which got miss"
                del missile_player2[0]
                attack_player1()


def attack_player1(flag=0):
    if len(missile_player1)==0:
        print "Player 1 has no missiles"
        flag_player1=1
        if flag==1:
            if len(player1)!=0 or len(player2)!=0:
                print("Peace")
                exit()
        else:
            attack_player2(flag_player1)
    else:
        m1=[]
        for m in missile_player1:
            m1.append(m)
        for i in m1:
            if i in player2:
                x=position_coordinate(i)
                print "Player 1 fires a missile with target"+x+" which got HIT"
                player2.remove(i)
                if len(player2)==0:
                    print("Player1 Won")
                    exit()
                del missile_player1[0]
                attack_player1()
            else:
                x=position_coordinate(i)
                print "Player-1 fires a missile with target "+x+" which got miss"
                del missile_player1[0]
                attack_player2()

attack_player1()

