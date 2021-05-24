# -*- coding: utf-8 -*-
"""
Author: Atte Järvinen, 2021
Description: Simulating games and training games between players
File: main.py
"""

from tictactoe import play_games, play_games_learning_graph
from random_player import RandomPlayer
from perfect_players import PerfectPlayers
from tabular_q_player import TabularQPlayer

RandomPlayer = RandomPlayer()
PerfectPlayers = PerfectPlayers()
TabularQPlayer1 = TabularQPlayer()
TabularQPlayer2 = TabularQPlayer()

#player1 = RandomPlayer.random_player
#player2 = RandomPlayer.random_player

#player1 = PerfectPlayers.perfect_player
player2 = PerfectPlayers.perfect_player

#player1 = PerfectPlayers.random_perfect_player
#player2 = PerfectPlayers.random_perfect_player

player1 = TabularQPlayer1.tabular_q_player
#player2 = TabularQPlayer1.tabular_q_player

#player1 = TabularQPlayer2.tabular_q_player
#player2 = TabularQPlayer2.tabular_q_player

#play 1000 games between players
play_games(1000, player1, player2)

#1000 training games between players
play_games_learning_graph(10, player1, player2)



