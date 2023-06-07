import random
import requests


def random_pokemon():
    pokemon_number = random.randint(1, 151)
    url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(pokemon_number)
    response = requests.get(url)
    pokemon = response.json()

    return {
        'name': pokemon['name'],
        'id': pokemon['id'],
        'height': pokemon['height'],
        'weight': pokemon['weight']
    }


def select_pokemon_computer():
    # Generates random pokemon, using def random_pokemon():
    pokemon_for_battle = random_pokemon()
    # Asks to choose stat for computer
    while True:
        print('Provide stat for computer you want to beet on(e.g. id, height, weight)')
        computer_stat = input()
        # takes user input and checks if the value is inside the dictionary
        if computer_stat in pokemon_for_battle:
            computer_stat = pokemon_for_battle[computer_stat]
            # prints the name of pokemon chosen
            print('You are fighting against: ' + pokemon_for_battle['name'])
            break
        # if value is not in the dictionary( for ex. typo)asks to provide it again
        else:
            print('Invalid value, try again')
    return computer_stat, pokemon_for_battle


def generate_random_pokemon_player():
    pokemon_list = {}

    for i in range(3):
        pokemon = random_pokemon()
        pokemon_list[f'p{i + 1}'] = pokemon

    for key, pokemon in pokemon_list.items():
        print(f'{key}: {pokemon}')

    while True:
        choice = input("Choose a pokemon for a battle (e.g., p1): ")
        chosen_pokemon = pokemon_list.get(choice)

        if chosen_pokemon is not None:
            print('Provide stat you want to bet on (e.g. id, height, weight)')
            user_stat = input()

            if user_stat in chosen_pokemon:
                user_stat = chosen_pokemon[user_stat]
                return user_stat, chosen_pokemon

            print("Invalid stat. Please try again.")
        else:
            print("Invalid choice. Please try again.")

    return None, None


def compare_stats(computer_stat, player_stat):
    # checks stats against each other, assigns the winner, returns winner
    if computer_stat > player_stat:
        winner = 'Computer'
        print('This round wins computer with stat {} against players stat {}'.format(computer_stat, player_stat))
    elif computer_stat < player_stat:
        winner = 'Player'
        print('This round player wins with stat {} against computers stat {}'.format(player_stat, computer_stat))
    else:
        winner = 'Tie'
        print('Tie computer stat {} and player stat {}'.format(computer_stat, player_stat))

    return winner


def record_scores(user_stat, computer_stat, chosen_pokemon, pokemon_for_battle, winner):
    with open('scores.txt', 'a') as file:
        file.write('User: {} ({}), Opponent: {} ({}), Stat: {}, Winner: {} \n'.format(
            chosen_pokemon['name'], chosen_pokemon['id'],
            pokemon_for_battle['name'], pokemon_for_battle['id'],
            computer_stat, user_stat, winner))


def record_total_scores(total_score_player, total_score_computer):
    with open('scores.txt', 'a') as file:
        file.write('Total score for three rounds for player is: {} and for computer is: {} \n'.format(
            total_score_player, total_score_computer))


def lets_play_again():
    # scores for three rounds
    total_score_computer = 0
    total_score_player = 0

    for _ in range(3):
        # declaring all the variables
        user_stat, chosen_pokemon = generate_random_pokemon_player()
        computer_stat, pokemon_for_battle = select_pokemon_computer()

        winner = compare_stats(computer_stat, user_stat)
        # Changes the score depending on who was the winner in the end of the round.

        if winner == 'Computer':
            total_score_computer += 1
            # Uses record_scores function to record the scores in scores.txt
            record_scores(user_stat, computer_stat, chosen_pokemon, pokemon_for_battle, winner)
        elif winner == 'Player':
            total_score_player += 1
            record_scores(user_stat, computer_stat, chosen_pokemon, pokemon_for_battle, winner)
        else:
            total_score_player = total_score_player
            total_score_computer = total_score_computer
            record_scores(user_stat, computer_stat, chosen_pokemon, pokemon_for_battle, winner)
        # Compares total scores and declares a winner

    if total_score_player > total_score_computer:
        print("Best pokemon fighter for today is player with score: computer {} vs player {} "
              .format(total_score_computer, total_score_player))
    elif total_score_player < total_score_computer:
        print("Best pokemon fighter for today is computer with score: computer {} vs player {} "
              .format(total_score_computer, total_score_player))
    else:
        print("It is a tie with score: computer {} vs player {}"
              .format(total_score_computer, total_score_player))

    return total_score_player, total_score_computer
