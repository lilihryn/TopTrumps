from main import select_pokemon_computer
from main import generate_random_pokemon_player
from main import compare_stats
from main import record_scores
from main import record_total_scores


def play_round():
    # variables for a single round
    user_stat, chosen_pokemon = generate_random_pokemon_player()
    computer_stat, pokemon_for_battle = select_pokemon_computer()
    winner = compare_stats(computer_stat, user_stat)
    # recording the round
    record_scores(user_stat, computer_stat, chosen_pokemon, pokemon_for_battle, winner)
    return winner


def top_trumps():
    total_score_player = 0
    total_score_computer = 0

    while True:
        winner = play_round()

        if winner == 'Computer':
            total_score_computer += 1
        elif winner == 'Player':
            total_score_player += 1

        if total_score_player >= 3 or total_score_computer >= 3:
            break

        # asking if the user wants to continue after each round
        print("Would you like to continue? (y/n)")
        answer = input().lower()

        if answer == 'n':
            print("See you later, Pokemon fighter")
            return

    # declaring the winner
    if total_score_player > total_score_computer:
        print("Best pokemon fighter for today is player with score: computer {} vs player {}"
              .format(total_score_computer, total_score_player))
        record_total_scores(total_score_player, total_score_computer)
    elif total_score_player < total_score_computer:
        print("Best pokemon fighter for today is computer with score: computer {} vs player {}"
              .format(total_score_computer, total_score_player))
        record_total_scores(total_score_player, total_score_computer)
    else:
        print("It is a tie with score: computer {} vs player {}"
              .format(total_score_computer, total_score_player))
        record_total_scores(total_score_player, total_score_computer)

    print("Would you like to play again? (y/n)")
    answer = input().lower()

    if answer == 'y':
        top_trumps()
    else:
        print("See you later, Pokemon fighter")


top_trumps()
