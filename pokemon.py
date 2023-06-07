# all the  imports
from main import select_pokemon_computer
from main import generate_random_pokemon_player
from main import compare_stats
from main import lets_play_again
from main import record_scores
from main import record_total_scores


def top_trumps():
    # variables for first round
    user_stat, chosen_pokemon = generate_random_pokemon_player()
    computer_stat, pokemon_for_battle = select_pokemon_computer()
    winner = compare_stats(computer_stat, user_stat)
    # recording first round
    record_scores(user_stat, computer_stat, chosen_pokemon, pokemon_for_battle, winner)
    # asking if user wants to play another game
    print("Would you like to continue y/n ")
    answer = input()
    # if yes, runs lets_play_again() and records total scores
    if answer == 'y':
        total_score_player, total_score_computer = lets_play_again()
        record_total_scores(total_score_player, total_score_computer)

    # if no

    else:
        print("See ya later, pokemon fighter")


top_trumps()
