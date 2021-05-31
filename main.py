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
    depth_limit = int(Val[3])
    time_out = float(Val[4])
    
elif Game_Type == 2: ## Loaded Game
   Val = RestoreGame()
   board = ToString(Val[0])
   player = int(Val[1])
   stealing = int(Val[2])
   depth_limit = int(Val[3])
   time_out = float(Val[4])
   Center_Drawing_String("--Your Game is being loaded--")
   print('\n')
   time.sleep(1)   
   print("Board=", Val[0])
   time.sleep(1)
   print("Player to play next= "+ Val[1])
   time.sleep(1)   
   print("Stealing Mode "+ Val[2])
   time.sleep(1)   
        
# TODO: When Ai play two times show to the user that he is going to play 2 times --> Done
# TODO: Add a condition on the pocket the Human choose, Between 7-12 --> Done
# TODO: Game difficulty Based on depth --> Done
# TODO: Clear the terminal after Every Play 
# TODO: Add the time Limit for the Human player --> Done 
# TODO: Add the bonus feature of saving and loading the Game --> Done
# TODO: Maybe Tweak the Save Game part so it wouldn't ask to save every 2 sec 


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
    # player 1 is AI
    if player == 1:  #AI will play
        next_board, next_player= playTurn(board, depth_limit, stealing)
        print_board(next_board)
        print("\n")
        if (player == next_player):    
            player=next_player
            board=next_board 
            Center_Drawing_String("--Player_1 got another turn--")
            print("\n")
        else:   
            player=next_player
            board=next_board
            Center_Drawing_String("--It's Human's Turn Now--")
            print("\n")
        
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

        print_board(next_board)
        print("\n")
        if (player == next_player):    
            player=next_player
            board=next_board 
            Center_Drawing_String("--Player_2 got another turn--")
            print("\n")
        else:   
            player=next_player
            board=next_board
            Center_Drawing_String("--It's AI's Turn Now--")
            print("\n")
            
    if (player != next_player):
        Center_Drawing_String_Circles(''' Would you like to save the game and continue later: Yes, No  ''')
        EndGame = input()
        if ((EndGame == 'Yes')): 
            SaveGame(next_board,next_player, stealing, depth_limit)
            sys.exit()
        
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
    
    
    
    