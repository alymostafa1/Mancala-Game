from Mancala_Project import *

# PLAYER 1

class Node:
    def __init__(self, board, maximizer=True):
        #self.depth = depth
        self.board = board
        self.possible_states = []
        self.score = None
        self.maximizer = maximizer
        self.alpha = float('-inf')
        self.beta = float('inf')
        
    def getStates(self, stealing = True):
        if self.maximizer:
            for i in range(6):
                possible_state, next_player = move(board, i, stealing)
                if next_player != -1:
                    state = Node(possible_state, next_player == 1)
                    self.possible_states.append(state)
        else:
            for i in range(7,13):
                possible_state, next_player = move(board, i, stealing)
                if next_player != -1:
                    state = Node(possible_state, next_player == 1)
                    self.possible_states.append(state)
    
    def buildTree(self, depth_limit, stealing = True):
        if depth_limit == 0:
            return 
        
        self.getStates(stealing)
        for state in self.possible_states:
            state.buildTree(depth_limit - 1, stealing)
                                                                    
        
    def minimax(self):
        
        if len(self.possible_states) == 0: ### GET SCORE
            score = self.board[6] - self.board[13]
            return score, None
        
        if gameover(self.board):
            #### FUNCTION TO COLLECT STONES IN EACH PLAYER'S MANCALA --- RETURN BOARD ####
            score = self.board[6] - self.board[13]
            return score, None
            
        best_state = None
        
        if self.maximizer: #### AI TURN - PLAYER1
            best = float('-inf')
            for state in self.possible_states:
                val, _ = state.minimax()
                self.alpha = max(self.alpha, val)
                if val > best:
                    best = val
                    best_state = state
                
                if self.beta <= self.alpha:
                    break
                
        else: 
            best = float('inf')
            for state in self.possible_states:
                val, _ = state.minimax()
                self.alpha = min(self.alpha, val)
                if val < best:
                    best = val
                    best_state = state
                    
                if self.beta <= self.alpha:
                    break
        
        return best, best_state.board
                
        # # if we reached the final node or the game is over before the depth limit 
        # if depth_limit == 0 or gameover(board)==1 :
        #     score= self.board[13] - self.board[6]
        #     return score
        
   
    def printMoves(self):
        for state in self.possible_states:
            print_board(state.board)
            print('\n\n\n')


board = [0,0,0,0,2,1,0,
         4,0,0,0,0,0,0]

game = Node(board)
game.buildTree(3, False)
score, best_state = game.minimax()
print(best_state)
print(score)
