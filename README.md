# Mancala Game
<div align="center">
   <strong>The World's Oldest Board Game </strong>  <br />  
   <br />
   <img src="https://user-images.githubusercontent.com/64116564/120125174-de702700-c1b7-11eb-9574-6418363c758a.png" />  
</div>   


 
**Mancala** is a two-player turn-based board game. It consists of 6 pits, 24 stones and a mancala for each player. Each mancala has to be on the right side of the player. The player should sit opposite to each other and play in **a counter-clockwise direction**.
 
As setup, Each pit should contain 4 stones except for the mancala. On each turn, the player will take all the stones from any of his/hers pit and deposit one stone in each pit. The player should skip his/hers opponent’s mancala. If the player's last stone lands in his/her own mancala, the player may take another turn.

**The Mancala game has two modes:** 
  * **Stealing**  
    ==> Stealing mode is if the player’s last stone lands on an empty pit, the player should capture the stones in his/her own pit and the stones in his/her opponent’s pit directly across the player’s pit.
  * **No Stealing.** 
 
**Game is OVER** when one of the player’s pits are all empty, by then the other player can capture all the stones left in his/her pits and place it in his/her mancala. **The winner** is the player with the most stones in his/her mancala. 

**The Mancala Game has 3 Difficulty Levels:**  
   * **Easy (Depth = 7)** ==> this takes less than 1 seconds.
   * **Intermediate ( Depth = 8)** ==> this takes less than 5 seconds.
   * **Hard ( Depth = 9)** ==> this takes around 23 seconds.  
   
## Algorithm:
**MiniMax with Alpha-beta pruning Algorithm** is used which is an ARTIFICIAL INTELLIGENCE solution for Game tress:
   * Expand the tree up to a certain tree depth and then stop. 
   * Evaluate leave nodes.
   * Label the two players as maximizer and minimizer. 
   * Propagate values from leaves to root node and choose the best possible move for the player:  
      * The maximizer (AI) chooses the move that returns the maximum possible value. 
      * The minimizer (The User) chooses the move that returns the minimum possible value.
## Implementation:

The Mancala project is implemented using Python3, The mancala algorithm is based on **minimax decision rule with alpha-beta pruning**. The player plays against an AI player using the console.    
The implementation consists of 3 source files: mancala, minimax and main. Each of these codes perform certain functions.   

**The mancala** file consists of 4 functions: 
   * print_board
   * getwinner
   * gameover 
   * move.  
   * SaveGame 
   * RestoreGame
   * NewGame 

**The minimax** file **consists of a class called Node** which contains 4 functions:  
   * getStates 
   * buildTree 
   * minimax 
   * print_moves.   

Lastly, **the main** file integrates both last 2 files and implement the game flow. 

## User Guide:
when you run the game, it asks you whether you want to start a new game or to load a previous game, then it prints the initial board in the 2 cases then it asks who you want to start the game whether it’s the AI or it’s you, then to choose the mode (Stealing or No Stealing), then to choose the game difficulty (Easy, Intermediate, Hard).

## Overview Demo:  
https://user-images.githubusercontent.com/64116564/121755074-8bcb2f00-cb16-11eb-962a-3286f9fa5aad.mp4  

**YouTube Link illustrating all the features:** https://www.youtube.com/watch?v=xORjiU3u55g&t=51s
## Requirements:
 * python 3.8.5
 
## Team Members:
  * Aly Moustafa El-Kady
  * Aya Tarek El-Ashry
  * Lama Zeyad Ibrahim
  * Yara Mohamed Zaki


