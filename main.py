
from minimax import *

board =[4,4,4,4,4,4,0,
        4,4,4,4,4,4,0]


print("to start first press 2 else press 1:")


player=int(input())

print("for stealing write 1 else write 0:")

stealing= int(input())

depth_limit=1 

while (gameover(board)!= 1):
    # player 1 is AI
    if player == 1:
        next_board, next_player= playTurn(board, depth_limit, stealing)
        player=next_player
        board=next_board
    
     
    #player 2 is the human 
    else: 
        print("Choose your pit:")
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
    
    