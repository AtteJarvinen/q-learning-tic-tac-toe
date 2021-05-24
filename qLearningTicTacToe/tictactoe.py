# -*- coding: utf-8 -*-
"""
Author: Atte Järvinen, 2021
Description: Tic Tac Toe and game simulation rules
File: tictactoe.py

"""
import numpy as np
import matplotlib.pyplot as plt

def new_board():
        
    return(np.array([[0, 0, 0],
                     [0, 0, 0],
                     [0, 0, 0]]))

def hash_value(board) -> int:
    
        hashValue = 0
    
        for i in range(len(board)):
            for j in range(len(board)):
        
                hashValue *= 3
                hashValue += board[i][j]
            
        return hashValue
    
def legal_moves(board):
        
        legalMoves = []
        
        for i in range(len(board)):
            for j in range(len(board)):
                
                if board[i][j] == 0:
                    legalMoves.append((i,j))
                    
        return legalMoves
    
def change_player(player):
    
        if player == 1:
            return 2
        else:
            return 1
        
def winner_check(board):

	winConditions = [[(0,0),(0,1),(0,2)], [(1,0),(1,1),(1,2)], [(2,0),(2,1),(2,2)], [(0,0),(1,0),(2,0)], 
					 [(0,1),(1,1),(2,1)], [(0,2),(1,2),(2,2)], [(0,0),(1,1),(2,2)], [(2,0),(1,1),(0,2)]]
	
	for i in winConditions:
	
		(first, second, third) = i
		
		if board[first] == board[second] == board[third] != 0:
		
			winner = board[first]
			return winner
	
	emptySpaces = legal_moves(board)
	
    #draw check
	if len(emptySpaces) == 0:
	
		return 3
		
	else:
	
		return 0
            
def play_game(player1, player2):
    
    player = 1
    result = 0      
    board = new_board()

    while result == 0:
    
        if player == 1:    
        
            board = player1(board, player)
            result = winner_check(board)
            player = change_player(player)
        
        else: 
        
            board = player2(board, player)
            result = winner_check(board)
            player = change_player(player)
        
    if result == 1:
        
        return 1
    
    elif result == 2:
        
        return 2
    
    elif result == 3:
        
        return 3
    
def play_games(games, player1, player2):
    
    numberOfGames = games
    result = 0
    player1Wins = 0
    player2Wins = 0
    draws = 0
    
    while games > 0:
        
        result = play_game(player1, player2)
        
        if result == 1:
            
            player1Wins += 1
        
        elif result == 2:
        
            player2Wins += 1
            
        elif result == 3:
            
            draws += 1
            
        games -= 1
        
    print("Player1 won ", player1Wins / numberOfGames)
    print("Player2 won ", player2Wins / numberOfGames)
    print("Draws ", draws / numberOfGames)
    
def play_learning_game(player1, player2):
    
    player = 1
    result = 0      
    board = new_board()

    while result == 0:
    
        if player == 1:    
        
            board = player1(board, player)
            result = winner_check(board)
            #to ensure we always update q-values
            if result != 0:                     
                  board = player2(board, player)  
            player = change_player(player)
        
        else: 
        
            board = player2(board, player)
            result = winner_check(board)
            #to ensure we always update q-values
            if result != 0:                     
                  board = player1(board, player)
            player = change_player(player)
        
    if result == 1:
        
        return 1
    
    elif result == 2:
        
        return 2
    
    elif result == 3:
        
        return 3
    
def play_learning_games(games, player1, player2):
    
    games = games
    result = 0
    player1Wins = 0
    player2Wins = 0
    draws = 0
        
    while games > 0:
            
        result = play_learning_game(player1, player2)
            
        if result == 1:
                
            player1Wins += 1
                
        elif result == 2:
            
            player2Wins += 1
                
        elif result == 3:
                
            draws += 1
                
        games -= 1
            
    return (player1Wins, player2Wins, draws)

#draw a graph about learning progress
def play_games_learning_graph(gameSeries, player1, player2, gamesInSeries = 100, loc='best'):
    
    player1Wins = []
    player2Wins = []
    draws = []
    count = []
    
    for i in range(gameSeries):
        
        player1Win, player2Win, draw = play_learning_games(gamesInSeries, player1, player2)
        
        player1Wins.append(player1Win*100.0/gamesInSeries)
        player2Wins.append(player2Win*100.0/gamesInSeries)
        draws.append(draw*100.0/gamesInSeries)
        count.append(i*gamesInSeries)
        
        player1Wins.append(player1Win*100.0/gamesInSeries)
        player2Wins.append(player2Win*100.0/gamesInSeries)
        draws.append(draw*100.0/gamesInSeries)
        count.append((i+1)*gamesInSeries)

    plt.ylabel('Results %')
    plt.xlabel('Games')

    plt.plot(count, player1Wins, 'r-', label='Player1 Wins')
    plt.plot(count, player2Wins, 'b-', label='Player2 Wins')
    plt.plot(count, draws, 'g-', label='Draws')
    plt.legend(loc=loc, shadow=True, fancybox=True, framealpha =0.7)
    