from Mancala_Project import *
import math

# PLAYER 1

class Node:
    def __init__(self, board):
        #self.depth = depth
        self.state = board
        self.possible_states = []
        self.score = None
        self.next_player = None
        self.alpha = -math.inf
        self.beta = math.inf
        
    def getStates(self):
        for i in range(6):
            possible_state, next_player = move(board, i)
            if possible_state != -1:
                state = Node(possible_state)
                self.next_player = next_player
                self.possible_states.append(state)
    
    def buildTree(self, depth_limit):
        if depth_limit == 0:
            return 
        
        self.getStates()
        for state in self.possible_states:
            state.buildTree(depth_limit - 1)
            
            
                                                                    
        
    def minimax(self,alpha, beta, depth_limit):
        max_layer =  self.next_player
        
        # if we reached the final node or the game is over before the depth limit 
        if depth_limit == 0 or gameover(board)==1 :
            score= self.board[13] - self.board[6]
            return score
        
    
        if max_layer == 1: #### AI TURN - PLAYER1
            best = -math.inf
            for state in self.possible_states:
                val = minimax(possible_states.state, depth_limit - 1)
                
                
                
        
        
    def printMoves(self):
        for state in self.possible_states:
            print_board(state.state)
            print('\n\n\n')



board = [4,4,4,4,4,4,0,
         4,4,4,4,4,4,0]

game = Node(board)
game.buildTree(2)
game.printMoves()
