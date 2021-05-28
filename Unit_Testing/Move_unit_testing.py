
from mancala_Game import *

'''
Unit Testing 
'''

'''
# Simple stone movement with zero rules
## Input:{ [5,4,4,4,4,4,4,4,4,4,4,4,4,4] , 0 }
## Expected output: [0, 5, 5, 5, 5, 5, 4, 4, 4, 4, 4, 4, 4, 4] , Next Player: 2
# Status: Done
'''

# board = [5,4,4,4,4,4,4,4,4,4,4,4,4,4]
# b, next_player = move(board, 0)
# print_board(b)
# print("Next player is: {}".format(int(next_player)))

'''
# Simple stone movement 
## input: board = [1,0,0,0,0,0, 0,    0,0,0,0,0,0, 0]
## Expected output: [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] , next player is 2
Status: Done
'''

# board=[1,0,0,0,0,0, 0,    0,0,0,0,0,0, 0]
# b, next_player = move(board, 0)
# print_board(b)
# print(b)
# print("Next player is: {}".format(int(next_player)))

'''
# Simple stone movement with round around 13 
## input: {board = [4,4,4,4,4,4,4,4,4,4,10,4,4,4]}
## Expected output: {board = [5,5,5,5,5,5,4,5,4,4,0,5,5,5]}
## State: Done
'''
# board = [4,4,4,4,4,4,4,4,4,4,10,4,4,4]
# b, next_player = move(board, 10)
# print_board(b)
# print("Next player is: {}".format(int(next_player)))


'''
# Testing round up around 13 and skipping opponent mancala 
## input:  board = [0,0,0,0,0,0, 0, 0,0,0,0,0,3, 0]
## Expected output:  [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], next player is 1
## Status: Done
'''
# board=[0,0,0,0,0,0, 0, 0,0,0,0,0,3, 0]
# b, next_player = move(board, 12)
# print_board(b)
# print(b)
# print("Next player is: {}".format(int(next_player)))


'''
# Testing round up around 13 and skipping opponent mancala 
## input:  board = [0,0,0,0,0,9, 0, 0,0,0,0,0,0, 0]
## Expected output:  [1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0], next player is 2
## Status: Done
'''
# board=[0,0,0,0,0,9, 0, 0,0,0,0,0,0, 0]
# b, next_player = move(board, 5)
# print_board(b)
# print(b)
# print("Next player is: {}".format(int(next_player)))


'''
# Testing if the final stop is at zero 
## Input: board=[0,0,0,0,10,0, 0,    0,0,0,0,0,0, 0]
## Expected output: [1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0]
## Status : Done
'''
# board=[0,0,0,0,10,0, 0,    0,0,0,0,0,0, 0]
# b, next_player = move(board, 4, False)
# print_board(b)
# print(b)
# print("Next player is: {}".format(int(next_player)))

'''
# Testing Stealing techniques 
## input: board=[0,0,0,0,10,0, 0,    0,0,0,0,0,0, 0]
## Expected output: [1, 0, 0, 0, 0, 1, 3, 1, 1, 1, 1, 0, 1, 0], next player is 2
## Status: Done
'''
# board=[0,0,0,0,10,0, 0,    0,0,0,0,0,0, 0]
# b, next_player = move(board, 4)
# print_board(b)
# print(b)
# print("Next player is: {}".format(int(next_player)))

'''
## Expected output: [1, 2, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0], next player is 2
'''
board=[0,1,0,0,10,0, 0, 0,0,0,0,0,0, 0]
b, next_player = move(board, 4, False)
print_board(b)
print(b)
print("Next player is: {}".format(int(next_player)))


