import pygame
from poker_bot.pygame.convert import convert_name, convert_suite


class Card:
    def __init__(self, card_value, card_suite, position_x, position_y):
        self.card_value = card_value
        self.card_suite = card_suite
        self.name = F"{card_value}_of_{card_suite}"
        self.image = pygame.image.load(F"../assets/PNG-cards-1.3/{self.name}.png")
        self.back_image = pygame.image.load(F"../assets/Card_back_01.svg.png")
        self.image = pygame.transform.scale(self.image, (100, 150))
        self.back_image = pygame.transform.scale(self.back_image, (100, 150))
        self.rect = self.image.get_rect()
        self.rect.x = position_x
        self.rect.y = position_y
        self.face_up = False

    def flip(self):
        self.face_up = not self.face_up

    def draw(self, screen):
        if self.face_up:
            screen.blit(self.image, self.rect)
        else:
            screen.blit(self.back_image, self.rect)

    def __str__(self):
        return self.name


def create_player_cards(players, position_x, position_y):
    players_cards = []
    for p in range(1, len(players)+1):
        players_cards.append([])
        for _card in players[p]:
            players_cards[p-1].append(Card(
                convert_name(_card[:-1]),
                convert_suite(_card[-1]),
                position_x,
                position_y))
            position_x += 110
        position_x -= 220
        position_y += 170
    return players_cards

def create_common_cards(common_cards, position_x, position_y):
    ccard = []
    for c in common_cards:
        ccard.append(Card(
            convert_name(c[:-1]),
            convert_suite(c[-1]),
            position_x,
            position_y))
        position_x += 110
    return ccard