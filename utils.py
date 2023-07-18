import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime, timezone


def get_players():
    players = pd.read_csv('players.csv')
    players = players[['name', 'date_of_birth', 'player_id']]
    return players.dropna()

def get_player(name):
    players = get_players()
    
    return players[players.name == name]

def verify_player_in_base(name):
    players = get_players()
    print()
    if len(players[players.name == name]) > 0:
        return True
    else:
        return False

def get_valuations():
    valuations = pd.read_csv('player_valuations.csv')
    valuations = valuations[['player_id', 'last_season', 'date', 'market_value_in_eur']]
    return valuations.dropna()

def get_stats():
    players = get_players()
    valuations = get_valuations()
    
    stats = valuations.merge(players, on='player_id', how='left')
    return stats

def show_player_history_value(player):
    x = player['date']
    y = player['market_value_in_eur']
    
    plt.figure(figsize=(16, 4))
    plt.plot(x, y, 'o--', color='blue')

    plt.ticklabel_format(axis='y', style='plain')
    plt.xticks(rotation=90)
    plt.grid()
    plt.show()

def year_to_timestamp(year):
    # Define a data do primeiro dia do ano às 00:00:00
    first_day_of_year = datetime(year, 1, 1, 0, 0, 0)

    # Converte a data para o formato de carimbo de data e hora (timestamp)
    timestamp = int(first_day_of_year.replace(tzinfo=timezone.utc).timestamp())
    
    return timestamp