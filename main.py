
from minimax import *
import time 
from os import system 

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
                      1.Stealing Mode
                      0.No Stealing Mode''')
                      
stealing= int(input())

print(''' Choose the game difficulty:
      1- Easy 
      2- Intermediate 
      3- Hard 
      ''')
     
depth_limit = int(input())

# TODO: When Ai play two times show to the user that he is going to play 2 times --> Done
# TODO: Add a condition on the pocket the Human choose, Between 7-12
# TODO: Game difficulty Based on depth 
# TODO: Clear the terminal after Every Play 
# TODO: Add the time Limti for the Human player 
# TODO: Add the bonus feature of saving and loading the Game 
#next_player=player

while (gameover(board)!= 1):
    # player 1 is AI
    if player == 1:  #AI will play
        next_board, next_player= playTurn(board, depth_limit, stealing)
        #print(next_player)
        #print(next_board, next_player)
        print_board(next_board)
        print("\n")
        if (player == next_player):    
            #print_board(next_board)
            player=next_player
            board=next_board 
            print("Player_1 got another turn \n")
            next_board, next_player= playTurn(board, depth_limit, stealing)
            #print(next_board, next_player)
            print_board(next_board)
            print("\n")
            player=next_player
            board=next_board 
            time.sleep(3)
            print("It's Now Human's Turn \n")
        else:   
            player=next_player
            board=next_board
            time.sleep(3)
            #print_board(next_board)
            print("It's Now Human's Turn \n")
        
    #player 2 is the human 
    else:  #Human will play
        print("Choose your pit [7-12]:   **Side-note: You have 15 seconds to choose**")
        t1 = time.time()
        idx =int(input())
        t2 = time.time()
        t=t2-t1
        if t > 15:
            print("You have run out of time!")
            break
        next_board, next_player =move(board,idx, stealing)
        #print(next_board, next_player)
        print_board(next_board)
        print("\n")
        player= next_player
        board= next_board
        print("It's Now AI's Turn \n")
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
    
    
    
    