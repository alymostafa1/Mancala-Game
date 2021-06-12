from minimax import *

greeting_list= ['XXXXXXXXXXXXXXXXXXXXXXXX' ,'--Welcome to Agmad-Mancala--', 'XXXXXXXXXXXXXXXXXXXXXXXX'] 
Center_Drawing_List(greeting_list)

print('''
      1. To start a new game
      2. To load previous game''')
Game_Type =  int(input())      
if Game_Type == 1: ## New Game
    Val = NewGame()
    board = Val[0]
    player = int(Val[1])
    stealing = int(Val[2])
    game_level = int(Val[3])
    
elif Game_Type == 2: ## Loaded Game
   Val = RestoreGame()
   board = ToString(Val[0])
   player = int(Val[1])
   stealing = int(Val[2])
   game_level = int(Val[3])

   Center_Drawing_String("--Your Game is being loaded--")
   print('\n')
   time.sleep(1)   
   print("Board=", Val[0])
   time.sleep(1)
   print("Player to play next= "+ Val[1])
   time.sleep(1)   
   print("Stealing Mode "+ Val[2])
   time.sleep(1)   

if game_level == 1:
    depth_limit = 7
elif game_level == 2:
    depth_limit = 8
elif game_level == 3:
    depth_limit = 9
else:
    depth_limit = 5
      
# TODO: When Ai play two times show to the user that he is going to play 2 times --> Done
# TODO: Add a condition on the pocket the Human choose, Between 7-12 --> Done
# TODO: Game difficulty Based on depth --> Done
# TODO: Clear the terminal after Every Play 
# TODO: Add the time Limit for the Human player --> Done 
# TODO: Add the bonus feature of saving and loading the Game --> Done
# TODO: Maybe Tweak the Save Game part so it wouldn't ask to save every 2 sec 

# FIXME: it's Ai turn Now is printed at the wrong time


if player == 1:
    Player_List = ['XXXXXXXXXXXXXXXXXXXXXXXX' ,'--Player_1 (AI) starts the game--', 'XXXXXXXXXXXXXXXXXXXXXXXX']
    Center_Drawing_List(Player_List)
    print("\n")
else:
    Player_List = ['XXXXXXXXXXXXXXXXXXXXXXXX' ,'--Player_2 (Human) starts the game--', 'XXXXXXXXXXXXXXXXXXXXXXXX']
    print("\n")
    Center_Drawing_List(Player_List)  
    print("\n")
time.sleep(3)  

while (gameover(board)!= 1):
    # counter =counter+1 
    # player 1 is AI
    if player == 1:  #AI will play
        next_board, next_player= playTurn(board, depth_limit, stealing)
        print_board(next_board)
        print("\n")
        
        if (player == next_player):    
            player=next_player
            board=next_board 
            Center_Drawing_String("-- Player 1 got another turn --")
            print("\n")
            
        else:               
            player=next_player
            board=next_board
            Center_Drawing_String_Circles('''Now, It's player 2 turn, Would you like to save the game and continue later: Y/N ?''')
            EndGame = input()
            if ((EndGame == 'Y' or EndGame =='y')): 
                SaveGame(next_board,next_player, stealing, depth_limit)
                sys.exit()     
            Center_Drawing_String("-- Player 2 is playing now --")
            print("\n")
        
    #player 2 is the human 
    else:  #Human will play
        print("Choose your pit [7-12]: ")

        idx =int(input())      
        while(idx < 7 or idx > 12):
            print("You entered wrong pocket index,, Please Re-enter your pit between [7-12]")
            idx=int(input())            

        
        next_board, next_player =move(board,idx, stealing)
        print_board(next_board)
        print("\n")

        if (player == next_player):    
            player=next_player
            board=next_board 
            Center_Drawing_String("--Player 2 got another turn--")
            print("\n")
        else:
            player=next_player
            board=next_board
            
            # save/load
            Center_Drawing_String_Circles('''Now, It's player 1 turn, Would you like to save the game and continue later: Y/N ?''')
            EndGame = input()
            if ((EndGame == 'Y' or EndGame =='y')): 
                SaveGame(next_board,next_player, stealing, depth_limit)
                sys.exit()   
            
            Center_Drawing_String("--Player 1 is playing Now--")
            print("\n") 
            
      
             

    

winner, board = getWinner(board)
if winner < 0 :
    print_board(board)
    print("player 2 is the winner")
elif winner > 0:
    print_board(board)
    print("Player 1 is the winner")
else:
    print("Tie")


    
    