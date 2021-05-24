# -*- coding: utf-8 -*-
"""
Author: Atte Järvinen, 2021
Description: Minimax algorithm and perfect/random-perfect player behaviour
File: perfect_players.py
"""
import random
from tictactoe import hash_value, winner_check, legal_moves, change_player

class PerfectPlayers:    

    def __init__(self):
    
        self.cache = {}
    
    #minimax algorithm
    def minimax(self, board, player):
    
        hashValue = hash_value(board)
        
        if hashValue in self.cache:          
            return self.cache[hashValue]
        
        result = winner_check(board)
        
        if result == 1:       
            return -1
        elif result == 2: 
            return 1
        elif result == 3:
            return 0
            
        if player == 1:
            
            best = 10
            
            for move in legal_moves(board):
                
                board[move] = player
                hashValue = hash_value(board)
                value = self.minimax(board, change_player(player))
                self.cache[hashValue] = value
                board[move] = 0
                
                if value < best:                    
                    best = value                    
                #best possible outcome, return best value here
                if best == -1:
                    self.cache[hashValue] = best
                    return best
                    
        elif player == 2:
            
            best = -10
            
            for move in legal_moves(board):
                
                board[move] = player
                hashValue = hash_value(board)
                value = self.minimax(board, change_player(player))
                self.cache[hashValue] = value
                board[move] = 0
                
                if value > best:                    
                    best = value                    
                #best possible outcome, return best value here
                if best == 1:
                    self.cache[hashValue] = best
                    return best
                    
        return best
    
    #perfect-player behaviour
    def perfect_player(self, board, player):
        
        result = winner_check(board)
        
        if result != 0:
            return board
        
        if player == 1: 
            a = 2
        else:
            a = -2
        
        for move in legal_moves(board):
            
            board[move] = player
            hashValue = hash_value(board)
            
            if hashValue in self.cache:                
                value = self.cache[hashValue]
            
            else:               
                value = self.minimax(board, change_player(player))
                self.cache[hashValue] = value
                
            board[move] = 0
            
            if player == 1:
                
                if value < a:                   
                    a = value
                    bestMove = move
            
            else:
                
                if value > a:              
                    a = value
                    bestMove = move
                
        board[bestMove] = player
                
        return board
    
    #random-perfect-player behaviour
    def random_perfect_player(self, board, player):
        
        result = winner_check(board)
        
        if result != 0:
            return board
    
        bestMoves = []
        
        if player == 1:
            a = 2
        else:
            a = -2
        
        for move in legal_moves(board):
            
            board[move] = player
            hashValue = hash_value(board)
            
            if hashValue in self.cache:             
                value = self.cache[hashValue]
            
            else:               
                value = self.minimax(board, change_player(player))
                self.cache[hashValue] = value
                
            board[move] = 0
            
            if player == 1:
                
                if value < a:                   
                    a = value
                    bestMoves.clear()
                    bestMoves.append(move)
                    
                elif value == a:               
                    bestMoves.append(move)
                
            else:
                
                if value > a:                
                    a = value
                    bestMoves.clear()
                    bestMoves.append(move)
                
                elif value == a:               
                    bestMoves.append(move)
                
        board[random.choice(bestMoves)] = player
                
        return board

