def checking_who_won_two_pair_scenario(players, number_of_two_pair):
    highest_number_of_pairs = 0
    bucket_of_potential_winners = []

    for k in range(1, len(players) + 1):
        pairs = number_of_two_pair[k]

        if len(pairs) > highest_number_of_pairs:
            highest_number_of_pairs = len(pairs)
            bucket_of_potential_winners = [k]
        elif len(pairs) == highest_number_of_pairs:
            max_pair_value = max(pairs) if pairs else -1

            # Set a very low initial value for the current_winner_pair_value
            current_winner_pair_value = float("-inf")

            # If there are potential winners, find the maximum pair value among them
            if bucket_of_potential_winners:
                current_winner_pair_value = max(number_of_two_pair[player][0] for player in bucket_of_potential_winners)

            if max_pair_value > current_winner_pair_value:
                bucket_of_potential_winners = [k]
            elif max_pair_value == current_winner_pair_value:
                bucket_of_potential_winners.append(k)

    return bucket_of_potential_winners
