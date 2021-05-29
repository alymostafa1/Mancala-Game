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

if player == 1:
    game = Node(board)
    game.buildTree(3, False)
    score, best_state = game.minimax()

    
