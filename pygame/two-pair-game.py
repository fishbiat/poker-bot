#!/bin/python

# Code for a simple pygame application that displays a pair of cards
# and allows the user to flip them over to see if they match.

# https://stackoverflow.com/questions/47639826/pygame-button-single-click

import pygame
import random
import poker_bot.functions as pb
from poker_bot.pygame.card import Card, create_player_cards, create_common_cards
from poker_bot.pygame.colors import BLACK, WHITE, GREEN, RED, POKER_GREEN
from poker_bot.pygame.convert import convert_name, convert_suite

# Create a deck of cards and 2 players
deck_of_cards = pb.create_deck_of_cards()
players = pb.create_players(2)

# Deal two cards each
for j in range(2):
    for i in players:   
        pb.deal_a_card(deck_of_cards, players[i])

# Burn cards and common cards
burned_cards = []
common_cards = []

# burn a single card:
pb.deal_a_card(deck_of_cards, burned_cards)

# The flop
for j in range(3):
    pb.deal_a_card(deck_of_cards, common_cards)

# The turn
pb.deal_a_card(deck_of_cards, burned_cards)
pb.deal_a_card(deck_of_cards, common_cards)

# The river
pb.deal_a_card(deck_of_cards, burned_cards)
pb.deal_a_card(deck_of_cards, common_cards)


print(players)
number_of_two_pair = pb.two_pairs_per_player(players)
pb.checking_who_won_two_pair_scenario(players, number_of_two_pair)


# Initialize Pygame
pygame.init()
clock = pygame.time.Clock()


# Set the height and width of the screen
screen_width = 700
screen_height = 800
screen = pygame.display.set_mode([screen_width, screen_height])
screen.fill(POKER_GREEN)


# Creat the images for the player's cards
position_x = 10
position_y = 300
player_cards = create_player_cards(players, position_x, position_y)

for p in range(0, len(players)):
    player_cards[p][0].flip()
    player_cards[p][1].flip()

# Create the images for the common cards
position_x = 80
position_y = 10
ccard = create_common_cards(common_cards, position_x, position_y)
for c in range(0, len(common_cards)):
    ccard[c].flip()

# PyGame Loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
          
    pygame.display.update()
  

    for p in range(0, len(players)):
        for count in range(2):
            player_cards[p][count].draw(screen)
    
    for c in range(0, len(common_cards)):
        ccard[c].draw(screen)

    # Part of event loop
    pygame.display.flip()
    clock.tick(30)

