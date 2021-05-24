# -*- coding: utf-8 -*-
"""
Author: Atte Järvinen, 2021
Description: Random player behaviour
File: random_player.py
"""
import random
from tictactoe import legal_moves, winner_check

class RandomPlayer:
    
    def __init__(self):
    
        self.possible_moves = []
    
    #random-player behaviour
    def random_player(self, board, player):
        
        result = winner_check(board)
        
        if result != 0:
            return board
        
        self.possible_moves = legal_moves(board)
        move = random.choice(self.possible_moves)
        board[move] = player
            
        return board