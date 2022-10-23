def checking_who_won_two_pair_scenario(players, number_of_two_pair):

    # When we start off, we haven't seen any pairs, so 
    # the highest we have seen starts at 0
    highest_number_of_pairs = 0

    # We haven't started looking at the hands yet, so this bucket of potential 
    # winners is empty
    bucket_of_potential_winners = []

    # We now loop through each player:
    for k in range(1, len(players) +1):

      # If the player has more pairs than the highest number of 
      # pairs we saw previously, then that player is our new potential 
      # winner, so empty the bucket of potential winners, and add
      # this player to that bucket
      if len(number_of_two_pair[k]) > highest_number_of_pairs:
        # Since this player has a higher number of pairs than
        # we have seen so far, the highest number of pairs is 
        # set to the number of pairs that they have
        highest_number_of_pairs = len(number_of_two_pair[k])
        # Empty the bucket 
        bucket_of_potential_winners = []
        # Add ths player to the bucket of winners
        bucket_of_potential_winners.append(k)

      # In certain circumstances, there will be players who have
      # the same amount of pairs, and in that case, both players 
      # should be in the bucket of potential winners
      elif len(number_of_two_pair[k]) == highest_number_of_pairs:
        # add the player who tied the previos top player to the
        # bucket of potential winners
        bucket_of_potential_winners.append(k)

    
    # The function has to output something that we can use
    return bucket_of_potential_winners
