def deal_a_card(source_deck, destination_bucket):
    card = random.choice(source_deck)
    source_deck.remove(card)
    destination_bucket.append(card)