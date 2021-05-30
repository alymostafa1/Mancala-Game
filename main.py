
from minimax import *
import time 

        
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

# TODO: When Ai play two times show to the user that he is going to play 2 times --> Done
# TODO: Add a condition on the pocket the Human choose, Between 7-12 --> Done
# TODO: Game difficulty Based on depth --> Done
# TODO: Clear the terminal after Every Play 
# TODO: Add the time Limit for the Human player --> Done 
# TODO: Add the bonus feature of saving and loading the Game 

if player == 1:
    print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
    print("Player_1 (AI) starts the game")
    print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
    print("\n")
else:
    print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
    print("Player_2 (Human) starts the game")
    print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")  
    print("\n")
while (gameover(board)!= 1):
    # player 1 is AI
    if player == 1:  #AI will play
        next_board, next_player= playTurn(board, depth_limit, stealing)
        #print(next_player)
        #print(next_board, next_player)
        print_board(next_board)
        print("\n")
        if (player == next_player):    
            player=next_player
            board=next_board 
            print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
            print("Player_1 got another turn")
            print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
            print("\n")
        else:   
            player=next_player
            board=next_board
            print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
            print("It's Human's Turn Now ")
            print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
        
    #player 2 is the human 
    else:  #Human will play
        print("Choose your pit [7-12]:   **Side-note: You have 15 seconds to choose**")
        t1 = time.time()
        idx =int(input())
        while(idx < 7 or idx > 12):
            print("You entered wrong pocket index,, Please Re-enter you pit between [7-12]")
            idx=int(input())
        t2 = time.time()
        t=t2-t1
        if t > time_out:
            print("You have run out of time!")
            break
        next_board, next_player =move(board,idx, stealing)
        #print(next_board, next_player)
        print_board(next_board)
        print("\n")
        if (player == next_player):    
            player=next_player
            board=next_board 
            print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
            print("Player_2 got another turn ")
            print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
            print("\n")
        else:   
            player=next_player
            board=next_board
            print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
            print("It's AI's Turn Now")
            print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")

    


if (gameover(board) != 1):  # Game ends because user is run out of time
    print("End 0f Game!")
else:
    winner= getwinner(board)
    if winner < 0 :
        print("player 2 is the winner")
    elif winner > 0:
        print("Player 1 is the winner")
    else:
        print("Tie")
    
    
    
    