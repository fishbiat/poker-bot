def two_pairs_per_player(players):
        
    # Create a bucket of buckets:
    number_of_two_pair = {}  # Think of this as an empty pick up truck bed

    
    # Loop through each of the players 
    for k in range(1, len(players) + 1):

        # Initiate the bucket first
        # Put an empty bucket in the back of the pickup truck for each player
        number_of_two_pair[k] = []
        
        # Goes through each players cards
        # Only has to loop through 6 of the 7 cards
        # because by the time we get to the 7th card, we've compared 
        # all cards
        for i in range(1, 7):
        
        # Also goes through each players cards
        # So that we can compare each card to each other
        for j in range(i+1,8):
            
            # Compare each cards
            compare_card_x = list(players[k][i-1])[0]
            compare_card_y = list(players[k][j-1])[0]

            # If the cards are equal 
            if compare_card_x == compare_card_y:
            # Then add the pair to the bucket of two pairs for that player 
            # BUT we ONLY need the face value, not both cards

            # We will use pair_simplifier(pair) to extract the face value
            face_value = pair_simplifier(F"{compare_card_x} {compare_card_y}")
            number_of_two_pair[k].append(face_value)
            
            # Print out the actual pairs for human readable
            print(F"Match is found!: Player {k}: {compare_card_x} {compare_card_y}")
        
        # Return a value

    return number_of_two_pair