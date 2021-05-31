import time 
import sys
from pytimedinput import timedInput

def print_board(board):
    print("| |" ,  board[12], "|" , board[11], "|"  , board[10], "|" , board[9], "|" , board[8], "|" , board[7], "| |" )
    # print("-----------------------------")
    print("|{}| \t\t\t\t\t  |{}|" .format(board[13], board[6]))
    # print("-----------------------------")
    print("| |",  board[0], "|" , board[1], "|"  , board[2], "|" , board[3], "|" , board[4], "|" , board[5], "| |" )

def ToString(String):
    List_2 = []
    String = str(String)[1:-2]
    String = String.replace(" ", "")
    List =  list(String.split(","))    
    for i in List:
        List_2.append(int(i))
    return List_2

def Center_Drawing_List(List ):

    for i in range(len(List)):
        txt = List[i]
        x = txt.center(80, 'X')
        print(x)

def Center_Drawing_String(String):
    x = String.center(80, 'X')
    print(x)

def Center_Drawing_String_Circles(String):
    x = String.center(80, 'O')
    print(x)
def Center_Drawing_String_Null(String):
    x = String.center(80)
    print(x)
        

def getWinner(board):
    board = board.copy()
    for i in range(6):
        board[6]+=board[i]
        board[i]=0
    for i in range(7,13):
        board[13]+=board[i]
        board[i]=0
        
<<<<<<< HEAD
    score = board[6] - board[13]
    return score 
 
def NewGame():
=======
    #score = board[6] - board[13]
    

    return board 
>>>>>>> bba6c61c6f73c5cd74b89ea6614c730066f03aa3
    
    board =[4,4,4,4,4,4,0,
        4,4,4,4,4,4,0]
    print_board(board)
    print("\n")
    print("Ai already won the name Player_1, You are now Player_2\n")
    print('''You may choose to Start first or Let your rival start first, You may select 1 or 2: 
          1. Show me your best move Ai!!!
          2. I will show you my move first''')
    player=int(input())
    
    print('''Plaese Choose: 
          0.No Stealing Mode
          1.Stealing Mode''')                      
    stealing= int(input())
    
    print(''' Choose the game difficulty:
          1- Easy 
          2- Intermediate 
          3- Hard 
          ''')     
    depth_limit = int(input())
    print("Enter the time you required to play ")
    time_out=int(input())
    
    return (board, player, stealing, depth_limit, time_out)
        
def SaveGame(next_board,next_player, stealing, depth_limit):
    with open("LastGame.txt", "w") as output:
            output.write(str(next_board))
            output.write('\n')
            output.write(str(next_player))
            output.write('\n')
            output.write(str(stealing))
            output.write('\n')
            output.write(str(depth_limit))
            output.write('\n')
            
def RestoreGame():
    f = open("LastGame.txt", "r")
    Game = []
    for x in f: 
        Game.append(x)
    return Game        
        
def gameover(board):
    count=0 
    count1=0
    for i in range(len(board)):
        if (i >= 0 and i < 6 ):
            if board[i] ==0:
                count = count + 1
                # print(count)
        elif ( i> 6 and i <13 ):
            if board[i]==0:
                count1 =count1 +1 
        
    if count == 6 or count1 == 6: 
        return 1        
    else: 
        return 0 
        
        
# result= gameover(board)
# print(result)

def move(board, idx, stealing = True):   
    player_1 = 0
    player_2 = 0 
    next_player = 0
    inc = 0
    final_idx = 0
    valid_stealing_flag = True
    board = board.copy()
    if idx < 6: 
         player_1 = 1
         next_player = 2
    else:
        player_2 = 2
        next_player =1

    pocket_val = board[idx]
    if pocket_val == 0 :
        # print("Pocket is empty")
        return board , -1    
    board[idx] = 0
    for i in range(idx + 1 , pocket_val + idx + 1):
        i = i%14
        final_idx = i 
        if ((player_1 == 1 and i == 13) or (player_2 == 2 and i == 6)):
            inc +=1
            continue
        else: 
            board[i] += 1 
            
    for i in range(inc):
        # TODO: Add a condition if the final_idx == 0, but dont increment the opponent mancala
            board[((final_idx + i + 1)%14)] += 1
            
    # Final position (Final pocket)            
    final_pos = (final_idx + inc) % 14      
    '''
     Valid stealing 
    '''      
    if (player_1 and final_pos > 6):
        valid_stealing_flag = False
    elif (player_2 and final_pos < 6): 
        valid_stealing_flag = False        
    '''
    Stealing technique
    '''
    if (final_pos != 6):
        if (final_pos != 13):            
            if (board[final_pos] == 1) and stealing == True and valid_stealing_flag == True:
                # will steal from 14 - ((final_idx + inc)%14) - 2  
                board[final_pos] += board[14 - final_pos - 2]
                board[14 - final_pos - 2] = 0
                if player_1: 
                    board[6] += board[final_pos]
                    board[final_pos] = 0           
                if player_2: 
                    board[13] += board[final_pos]
                    board[final_pos] = 0  
                    
    if(player_1 and (final_pos) == 6) :
        next_player = 1    
    elif (player_2 and (final_pos == 13)) :  # Final play          
        next_player = 2
                    
    return board , next_player
    

# #   [0,1,2,3,4 ,5,6,7,8,9,10,11,12,13]

#board=[0,0,0,0,2,1, 1,    1,0,0,0,0,0, 0] 
#b, next_player = move(board, 7)
#print_board(b)
#print(b)
#print("Next player is: {}".format(int(next_player)))

# w = NewGame()
# print(w[0])

# w = RestoreGame()
# print(w[2])

# List = "[4, 4, 0, 5, 5, 5, 1, 4, 4, 4, 4, 4, 4, 0]"
# print(ToString(List))


