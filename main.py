
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
                      1.Stealing Mode
                      0.No Stealing Mode''')
stealing= int(input())
depth_limit = 1 

# TODO: When Ai play two times show to the user that he is going to play 2 times --> Done
# TODO: Add a condition on the pocket the Human choose, Between 7-12
# TODO: Game difficulty Based on depth 
# TODO: Clear the terminal after Every Play 
# TODO: Add the time Limti for the Human player 
# TODO: Add the bonus feature of saving and loading the Game 
while (gameover(board)!= 1):
    # player 1 is AI
    if player == 1:
        next_board, next_player= playTurn(board, depth_limit, stealing)
        if (player == next_player): 
            print("Player_1 got another turn \n")            
            print_board(next_board)
            player=next_player
            board=next_board            
            time.sleep(3)
        else:   
            time.sleep(3)
            player=next_player
            board=next_board
            print_board(next_board)
            print("It's Now your Turn \n")
        
    
     
    #player 2 is the human 
    else: 
        print("Choose your pit [7-12]:")
        idx =int(input())
        next_board, next_player =move(board,idx-1, stealing)
        player= next_player
        board= next_board

winner= getwinner(board)

if winner < 0 :
    print("player 2 is the winner")
elif winner >0:
    print("Player 1 is the winner")
else:
    print("Tie")
    
    