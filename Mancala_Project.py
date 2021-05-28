def print_board(board):
    print("| |" ,  board[12], "|" , board[11], "|"  , board[10], "|" , board[9], "|" , board[8], "|" , board[7], "| |" )
    # print("-----------------------------")
    print("|{}| \t\t\t\t\t  |{}|" .format(board[13], board[6]))
    # print("-----------------------------")
    print("| |",  board[0], "|" , board[1], "|"  , board[2], "|" , board[3], "|" , board[4], "|" , board[5], "| |" )

def move(board, idx, stealing = True):   
    player_1 = 0
    player_2 = 0 
    next_player = 0
    inc = 0
    final_idx = 0
    board = board.copy()
    if idx < 6: 
         player_1 = 1
    else:
        player_2 = 2

    pocket_val = board[idx]
    if pocket_val == 0 :
        print("Pocket is empty")
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
        if final_idx == 0 : # Final idx = 0 and inc range(1), 0+0
            board[(final_idx + i + 1)] += 1
        else:     
            board[(final_idx + i)] += 1
        
    if(player_1 and ((final_idx + inc) % 14) == 6) or player_2:
        next_player = 1    
    elif (player_2 and ((final_idx+inc)%14) == 13) or player_1 :  # Final play          
        next_player = 2
        
    '''
    Stealing technique
    '''
    if (board[((final_idx + inc) % 14)] == 1) and stealing == True :
        
        # will steal from 14 - ((final_idx + inc)%14) - 2  
        board[((final_idx + inc) % 14)] += board[(14 - (final_idx + inc) % 14) - 2]
        board[(14 - (final_idx + inc) % 14) - 2] = 0
        if player_1: 
            board[6] += board[((final_idx + inc) % 14)]
            board[((final_idx + inc) % 14)] = 0           
        if player_2: 
            board[13] += board[((final_idx + inc) % 14)]
            board[((final_idx + inc) % 14)] = 0      
    return board , next_player
    
board=[0,0,0,0,0,0,0,0,0,0, 0, 0, 0, 0]
#     [0,1,2,3,4 ,5,6,7,8,9,10,11,12,13]
b, next_player = move(board, 4, False)
print_board(b)
print(b)
print("Next player is: {}".format(int(next_player)))








