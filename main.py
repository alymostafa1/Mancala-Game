# -*- coding: utf-8 -*-
"""
Created on Sat May 29 20:34:42 2021

@author: Aya El Ashry
"""

from minimax import *

board =[4,4,4,4,4,4,0,
        4,4,4,4,4,4,0]


print("to start first press 1 else press 2:")


player=int(input())

print("for stealing write True else write False:")

stealing= string(input())

# first 
if player == 1: # player 1 is AI
    game = Node(board)
    game.buildTree(3, False)
    score, board = game.minimax()
    
#player 2 is the human 
else: 
    print("Choose your pit:")
    idx =int(input())
    board, next_player =move(board,idx-1, stealing)
    

