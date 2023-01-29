
from flask import Flask, render_template
import poker_bot.functions as pb

app = Flask(__name__,
            static_url_path='',
            static_folder='assets',
            template_folder='templates')

def convert_name(letter):
    if letter == "j":
        return "jack"
    if letter == "q":
        return "queen"
    if letter == "k":
        return "king"
    if letter == "a":
        return "ace"
    return letter

def convert_suite(letter):
    if letter == "H":
        return "hearts"
    if letter == "D":
        return "diamonds"
    if letter == "C":
        return "clubs"
    if letter == "S":
        return "spades"

def card_image_location(card_value, card_suite):
    name = F"{card_value}_of_{card_suite}"
    return F"/PNG-cards-1.3/{name}.png"


def get_card_images(card_array):
    cimgs = []
    for c in card_array:
        cimgs.append(card_image_location(
                     convert_name(c[:-1]),
                     convert_suite(c[-1])))
    return cimgs

@app.route('/')
def root():
    return "/two_pair"

@app.route('/two_pair')
def two_pair():
     # Create a deck of cards and 2 players
    deck_of_cards = pb.create_deck_of_cards()
    players = pb.create_players(2)

    # Deal two cards each
    for j in range(2):
        for i in players:   
            pb.deal_a_card(deck_of_cards, players[i])

    p1imgs=get_card_images(players[1])
    p2imgs=get_card_images(players[2])
    
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
    for key, value in players.items():
        players[key] = value + common_cards
    print(players)

    number_of_two_pair = pb.two_pairs_per_player(players)
    winner = pb.checking_who_won_two_pair_scenario(players, number_of_two_pair)

    return render_template('index.html',
                           ccimgs=get_card_images(common_cards),
                           p1imgs=p1imgs,
                           p2imgs=p2imgs,
                           number_of_two_pair=number_of_two_pair,
                           winner=winner)

app.run(host='0.0.0.0', port=8080, debug=True)