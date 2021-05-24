# -*- coding: utf-8 -*-
"""
Author: Atte Järvinen, 2021
Description: Tabular Q-agent implementation and q-player behaviour
File: tabular_q_player.py
"""
from tictactoe import hash_value, winner_check

class TabularQPlayer:
    
    def __init__(self):
    
        self.winValue = 1.0
        self.drawValue = 0.5
        self.lossValue = 0.0
    
        self.q = {} #list of Q-tables
        self.moveHistory = []
        
        self.initialQValue = 0.6
        self.learningRate = 0.9
        self.rewardDiscount = 0.95
        
        self.training = True
    
    #initialize Q-values
    def init_q_table(self, board):
        
        legalMoves = []
        
        for i in range(len(board)):
            for j in range(len(board)):
                
                if board[i][j] == 0:
                    legalMoves.append(self.initialQValue)
                else:
                    legalMoves.append(-1)
        
        return legalMoves
    
    #find Q-table for a state
    def find_q_values(self, board):
    
        hashValue = hash_value(board)
        
        if hashValue in self.q:
            qValues = self.q[hashValue]
        else:
            qValues = self.init_q_table(board)
            self.q[hashValue] = qValues
            
        return qValues
    
    #find a move based on Q-table index
    def index_to_move(self, index):

        moves = [(0,0), (0,1), (0,2), (1,0), (1,1), 
                 (1,2), (2,0), (2,1), (2,2)]
        move = moves[index]
        return move
    
    #Q-value updates based on the game result
    def update_q_values(self, result):
    
        newMax = -1.0
        self.moveHistory.reverse()
        
        #player 1 wins
        if result == 1:       
            for i in self.moveHistory:
                (hashValue, move, player) = i
                if player == 1:        
                    qValues = self.q[hashValue]
                    if newMax < 0:
                        qValues[move] = self.winValue
                        self.q[hashValue] = qValues
                    else:
                        qValues[move] = (qValues[move] * (1.0 - 
                                                          self.learningRate) + 
                                         self.learningRate * 
                                         self.rewardDiscount * newMax)
                        self.q[hashValue] = qValues                
                    newMax = max(qValues)
                elif player == 2:
                    qValues = self.q[hashValue]
                    if newMax < 0:
                        qValues[move] = self.lossValue
                        self.q[hashValue] = qValues
                    else:
                        qValues[move] = (qValues[move] * (1.0 - 
                                                          self.learningRate) + 
                                         self.learningRate * 
                                         self.rewardDiscount * newMax)
                        self.q[hashValue] = qValues                
                    newMax = max(qValues)

        #player 2 wins
        elif result == 2:
            for i in self.moveHistory:
                (hashValue, move, player) = i
                if player == 1:        
                    qValues = self.q[hashValue]
                    if newMax < 0:
                        qValues[move] = self.lossValue
                        self.q[hashValue] = qValues
                    else:
                        qValues[move] = (qValues[move] * (1.0 - 
                                                          self.learningRate) + 
                                         self.learningRate * 
                                         self.rewardDiscount * newMax)
                        self.q[hashValue] = qValues               
                    newMax = max(qValues)
                elif player == 2:
                    qValues = self.q[hashValue]
                    if newMax < 0:
                        qValues[move] = self.winValue
                        self.q[hashValue] = qValues
                    else:
                        qValues[move] = (qValues[move] * (1.0 - 
                                                          self.learningRate) + 
                                         self.learningRate * 
                                         self.rewardDiscount * newMax)
                        self.q[hashValue] = qValues                
                    newMax = max(qValues)
        
        #game ends in a draw
        elif result == 3:
            for i in self.moveHistory:
                (hashValue, move, player) = i
                qValues = self.q[hashValue]
                if newMax < 0:
                    qValues[move] = self.drawValue
                    self.q[hashValue] = qValues
                else:
                    qValues[move] = (qValues[move] * (1.0 - 
                                                          self.learningRate) + 
                                         self.learningRate * 
                                         self.rewardDiscount * newMax)
                    self.q[hashValue] = qValues
                newMax = max(qValues)
    
    #q-player behaviour
    def tabular_q_player(self, board, player):
    
        result = winner_check(board)
        
        if result != 0 and self.training == True:
            self.update_q_values(result)
            self.moveHistory.clear()
            self.bs =+1
            return board
        elif result != 0 and self.training == False:
            self.moveHistory.clear()
            return board
    
        qValues = self.find_q_values(board)
        maxValue = max(qValues)
        
        index = 0
        
        for i in qValues:
            
            if i == maxValue:
                
                break
            
            index += 1
        
        move = self.index_to_move(index)
        hashValue = hash_value(board)
        self.moveHistory.append((hashValue, index, player))
        board[move] = player
        
        result = winner_check(board)
        
        if result != 0 and self.training == True:
            self.update_q_values(result)
            self.moveHistory.clear()
            self.bs =+1
            return board
        elif result != 0 and self.training == False:
            self.moveHistory.clear()
            return board
        elif result == 0:
            return board