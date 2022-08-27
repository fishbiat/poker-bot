def create_deck_of_cards():  
  card_numbers = [2,3,4,5,6,7,8,9,10]
  card_royality = ["j","q","k","a"]
  card_suites = ["H","D","S","C"]
  card_faces = card_numbers+card_royality
  deck_cards = []
  for i in card_suites:
    for j in card_faces:
      deck_cards.append(F"{j}{i}")
  return deck_cards