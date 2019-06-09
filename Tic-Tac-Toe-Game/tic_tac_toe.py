position={'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}

def board_print():
    print('   |   |   ')
    print('',position['1'],'|',position['2'],'|',position['3'],' ')
    print('___|___|___')
    print('   |   |   ')
    print('',position['4'],'|',position['5'],'|',position['6'],' ')
    print('___|___|___')
    print('   |   |   ')
    print('',position['7'],'|',position['8'],'|',position['9'],' ')
    print('   |   |   ')

def match(player,var,m):
    if position['1']==var and position['2']==var and position['3']==var:
        print('Game Over!!! ',player,' won')
        flag=0
        return flag
    elif position['4']==var and position['5']==var and position['6']==var:
        print('Game Over!!! ',player,' won')
        flag=0
        return flag
    elif position['7']==var and position['8']==var and position['9']==var:
        print('Game Over!!! ',player,' won')
        flag=0
        return flag
    elif position['1']==var and position['4']==var and position['7']==var:
        print('Game Over!!! ',player,' won')
        flag=0
        return flag
    elif position['2']==var and position['5']==var and position['8']==var:
        print('Game Over!!! ',player,' won')
        flag=0
        return flag
    elif position['3']==var and position['6']==var and position['9']==var:
        print('Game Over!!! ',player,' won')
        flag=0
        return flag
    elif position['1']==var and position['5']==var and position['9']==var:
        print('Game Over!!! ',player,' won')
        flag=0
        return flag
    elif position['3']==var and position['5']==var and position['7']==var:
        print('Game Over!!! ',player,' won')
        flag=0
        return flag
    elif m==8:        
        print('Match Draw!!!')
        flag=0
        return flag
        
board_print()
player1=input('Player1 : Please choose \'X\' or \'O\':')

if player1.upper()=='X':
    print('Player1 : X \n\n\nPlayer2 : O\n\n\nPlayer1 turn!!!')
    temp=[]
    move=0
    end=1
    N=0
    Q=0
    while move<9:
        if len(temp)%2==0:
            while int(N)<1 or int(N)>9 or N in temp:
                N=input('Player1:Enter your choise(1-9):')
            temp.append(N)
            position[N]='X'
            board_print()
            end=match('Player1','X',move)
            if end==0:
                break
        else:
            while int(Q)<1 or int(Q)>9 or Q in temp:
                Q=input('Player2:Enter your choise(1-9):')
            temp.append(Q)
            position[Q]='O'
            board_print()
            end=match('Player2','O',move)
            if end==0:
                break            
        move=move+1
else:
    print('Player2 : X \n\n\nPlayer1 : O\n\n\nPlayer2 turn!!!')
    temp=[]
    move=0
    N=0
    Q=0
    while move<9:
        if len(temp)%2==0:
            while int(N)<1 or int(N)>9 or N in temp:
                N=input('Player2:Enter your choise(1-9):')
            temp.append(N)
            position[N]='X'
            board_print()
            end=match('Player2','X',move)
            if end==0:
                break
        else:
            while int(Q)<1 or int(Q)>9 or Q in temp:
                Q=input('Player1:Enter your choise(1-9):')
            temp.append(Q)
            position[Q]='O'
            board_print()
            end=match('Player1','O',move)
            if end==0:
                break
        move=move+1
x=input()

