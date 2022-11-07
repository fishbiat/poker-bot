#!/bin/python

# Code for a simple pygame application that displays a pair of cards
# and allows the user to flip them over to see if they match.

import pygame
import random

position_x = 10
position_y = 100

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
POKER_GREEN = (53,101,77)

card_value = ""
card_suite = ""

class Card:
    def __init__(self, card_value, card_suite, position_x, position_y):
        self.card_value = card_value
        self.card_suite = card_suite
        self.name = F"{card_value}_of_{card_suite}"
        self.image = pygame.image.load(F"../assets/PNG-cards-1.3/{self.name}.png")
        self.image = pygame.transform.scale(self.image, (100, 150))
        self.rect = self.image.get_rect()
        self.rect.x = position_x
        self.rect.y = position_y
        self.face_up = True

    def flip(self):
        self.face_up = not self.face_up

    def draw(self, screen):
        if self.face_up:
            screen.blit(self.image, self.rect)
        else:
            pygame.draw.rect(screen, BLACK, self.rect)

    def __str__(self):
        return self.name

# # This class represents a card
# class Card(pygame.sprite.Sprite):
#     # Constructor. Pass in the color of the card, and its x and y position
#     def __init__(self, color, width, height):
#         # Call the parent class (Sprite) constructor
#         super().__init__()

#         # Create an image of the block, and fill it with a color.
#         # This could also be an image loaded from the disk.
#         self.image = pygame.Surface([width, height])
#         self.image.fill(color)

#         # Fetch the rectangle object that has the dimensions of the image.
#         # Update the position of this object by setting the values of rect.x and rect.y
#         self.rect = self.image.get_rect()

# Initialize Pygame
pygame.init()
clock = pygame.time.Clock()


# Set the height and width of the screen
screen_width = 700
screen_height = 400
screen = pygame.display.set_mode([screen_width, screen_height])
screen.fill(POKER_GREEN)


card1 = Card("2", "clubs", position_x, position_y)
position_x += 110
card2 = Card("5", "diamonds", position_x, position_y)


# image1 = pygame.image.load('PNG-cards-1.3/2_of_clubs.png')
# image1 = pygame.transform.scale(image1, DEFAULT_IMAGE_SIZE)

# image2 = pygame.image.load('PNG-cards-1.3/5_of_diamonds.png')
# image2 = pygame.transform.scale(image2, DEFAULT_IMAGE_SIZE)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
          
    pygame.display.update()
    #screen.fill(POKER_GREEN)

    # # Show the image
    # screen.blit(image1, (100, 100))
    # screen.blit(image2, (220, 100))
  

    card1.draw(screen)
    card2.draw(screen)

    # Part of event loop
    pygame.display.flip()
    clock.tick(30)

# This is a list of 'sprites.' Each block in the program is
# added to this list. The list is managed by a class called 'Group.'
# card_list = pygame.sprite.Group()

# # This is a list of every sprite. All blocks and the player block as well.
# all_sprites_list = pygame.sprite.Group()

# for i in range(50):
#     # This represents a block
#     card = Card(POKER_GREEN, 20, 15)

#     # Set a random location for the block
#     card.rect.x = random.randrange(screen_width)
#     card.rect.y = random.randrange(screen_height)

#     # Add the block to the list of objects
#     card_list.add(card)
#     all_sprites_list.add(card)

# # Create a RED player block
# player = Card(RED, 20, 15)
# all_sprites_list.add(player)


# # Loop until the user clicks the close button.
# done = False

# # Used to manage how fast the screen updates
# clock = pygame.time.Clock()

# # -------- Main Program Loop -----------
# while not done:
#     for event in pygame.event.get():  # User did something
#         if event.type == pygame.QUIT:  # If user clicked close
#             done = True  # Flag that we are done so we exit this loop

#     # Clear the screen
#     screen.fill(POKER_GREEN)

#     # Get the current mouse position. This returns the position
#     # as a list of two numbers.
#     pos = pygame.mouse.get_pos()

#     # Fetch the x and y out of the list,
#     # just like we'd fetch letters out of a string.
#     # Set the player object to the mouse location
#     player.rect.x = pos[0]
#     player.rect.y = pos[1]

#     # See if the player block has collided with anything.
#     blocks_hit_list = pygame.sprite.spritecollide(player, card_list, True)

#     # Check the list of collisions.
#     for block in blocks_hit_list:
#         print("Block collided")

#     # Draw all the spites
#     all_sprites_list.draw(screen)

#     # Go ahead and update the screen with what we've drawn.
#     pygame.display.flip()

#     # Limit to 60 frames per second
#     clock.tick(60)
    
#     # Close the window and quit.
# pygame.quit()
    



