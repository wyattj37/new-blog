#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 23 13:54:43 2023

@author: wyattjohnston
"""

import matplotlib.pyplot as plt

times = [3.5, 3.5, 3.5, 3.5, 3.5, 3.5, 3.5, 3.5, 3.5, 8, 8, 8, 8, 8, 12, 50, 3.5, 3.5, 3.5, 50, 3.5, 3.5, 3.5, 18, 3.5, 3.5, .5, 3.5, 3.5, 3.5, 3.5, 3.5, 3.5, 12]

def thunderstruck(num_players):
    player_list = [0]*num_players
    for i,_ in enumerate(times):
        player_list[i%num_players] += times[i]
    return player_list
    

def create_graphs(players):
    drinks = thunderstruck(players)
    
    x_labels = [f"Player {i}" for i in range(1, len(drinks) + 1)]
    
    if (players > 4 and players < 12):
        max_idx = drinks.index(max(drinks))
        max_idx2 = drinks.index(max(drink for drink in drinks if drink != max(drinks)))
        colors = ['red' if i == max_idx or i ==  max_idx2 else 'grey' for i in range(len(drinks))]
    elif (players >= 12 and players != 14):
        max_idx = drinks.index(max(drinks))
        max_idx2 = max_idx + 4
        colors = ['red' if i == max_idx or i ==  max_idx2 else 'grey' for i in range(len(drinks))]
    elif (players == 14):
        max_idx = drinks.index(max(drinks))
        max_idx2 = max_idx - 4
        colors = ['red' if i == max_idx or i ==  max_idx2 else 'grey' for i in range(len(drinks))]
    else:
        max_idx = drinks.index(max(drinks))
        colors = ['red' if i == max_idx else 'grey' for i in range(len(drinks))]
    plt.bar(x_labels, drinks, color=colors)
    
    plt.ylabel('Seconds Drinking')
    plt.title('Thunderstruck')
    
    if (i > 7):
        plt.xticks(rotation=45)
    plt.tight_layout()

    plt.show()

for i in range(2,15):
    create_graphs(i)
