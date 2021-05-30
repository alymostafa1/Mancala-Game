from Mancala_Project import *

# PLAYER 1

def playTurn(board, depth_limit, stealing = True):
    game = Node(board)
    game.buildTree(depth_limit, stealing)
    score, best_state, best_player = game.minimax()
    
    return best_state, best_player


class Node:
    def __init__(self, board, maximizer=True):
        #self.depth = depth
        self.board = board
        self.possible_states = []
        self.next_players=[]
        self.score = None
        self.maximizer = maximizer
        self.alpha = float('-inf')
        self.beta = float('inf')
        
    def getStates(self, stealing = True):
        if gameover(self.board):
            return
        
        if self.maximizer:
            for i in range(6):
                possible_state, next_player = move(self.board, i, stealing)
                if next_player != -1:
                    state = Node(possible_state, next_player == 1)
                    self.possible_states.append(state)
                    self.next_players.append(next_player)
                    #print("next player:", next_player)
                    #print(possible_state)
                
                
        else:
            for i in range(7,13):
                possible_state, next_player = move(self.board, i, stealing)
                if next_player != -1:
                    state = Node(possible_state, next_player == 1)
                    self.possible_states.append(state)
                    self.next_players.append(next_player)
                    #print("next player:", next_player)
                    #print(possible_state)
                
                
    def buildTree(self, depth_limit, stealing = True):
        #print("Depth", depth_limit)
        if depth_limit == 0:
            #print("game over")
            return 
        
        self.getStates(stealing)
        for state in self.possible_states:
            state.buildTree(depth_limit - 1, stealing)
                                                                    
        
    def minimax(self):
        
        if gameover(self.board):
            score = getWinner(self.board)
            return score, None, None
        
        if len(self.possible_states) == 0: ### GET SCORE
            score = self.board[6] - self.board[13]
            return score, None, None
            
        best_state = None
        best_player= None
        if self.maximizer: #### AI TURN - PLAYER1
            best = float('-inf')
            for state in self.possible_states:
                
                val= state.minimax()
             
                self.alpha = max(self.alpha, val[0])
                if val[0] > best:
                    index= self.possible_states.index(state)
                    #print("index is:",index)
                    best_player= self.next_players[index]
                    best = val[0]
                    best_state = state
                
                if self.beta <= self.alpha:
                    break
                
        else: 
            best = float('inf')
           
            for state in self.possible_states:
         
                val= state.minimax()
              
                self.alpha = min(self.alpha, val[0])
                if val[0] < best:
                    index= self.possible_states.index(state)
                    #print("index is:",index)
                    best_player= self.next_players[index]
                    best = val[0]
                    best_state = state
                    

                if self.beta <= self.alpha:
                    break
        #print("best player:",best_player)
        
        return best, best_state.board, best_player 
   
    def printMoves(self):
        for state in self.possible_states:
            print_board(state.board)
            print('\n\n\n')



board=[1,0,0,0,2,1, 0,    1,0,0,0,0,0, 0]

depth_limit = 8
stealing = True
best_state = playTurn(board, depth_limit, stealing)
print("best_state is :",best_state)
