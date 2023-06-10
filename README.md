

# Pokémon Battle Game

This is a simple command-line game where you can battle against the computer using randomly selected Pokémon and their stats. The game involves selecting a Pokémon and choosing a specific stat to compete against the computer. The player and the computer compare their chosen stats, and the winner of each round is recorded. The game continues until either the player or the computer reaches a score of 3. At the end of the game, the overall winner is declared, and the scores are recorded.

## Installation

1. Clone the repository to your local machine using the following command:
   ```
   git clone <repository_url>
   ```

2. Navigate to the project directory:
   ```
   cd pokemon-battle-game
   ```

3. Install the required dependencies by running:
   ```
   pip install -r requirements.txt
   ```

## How to Play

1. Run the game by executing the following command:
   ```
   python main.py
   ```

2. The game will prompt you to select a Pokémon and a stat to bet on. Follow the on-screen instructions to make your choices.

3. The computer will randomly select a Pokémon and a stat to compete against you.

4. The stats will be compared, and the winner of the round will be determined.

5. The round results, including the chosen Pokémon, stats, and the winner, will be recorded in the 'scores.txt' file.

6. Play rounds until either the player or the computer reaches a score of 3.

7. At the end of the game, the overall winner will be declared based on the total scores, and the final scores will be recorded in the 'scores.txt' file.

8. You will be asked if you want to play again. Choose 'y' to play another game or 'n' to exit.

## File Descriptions

- `main.py`: Contains the main game logic and functions for playing rounds, comparing stats, and recording scores.
- `scores.txt`: A text file that records the results of each round and the total scores.

## Dependencies

The game relies on the following dependencies, which can be installed using `pip`:
- `requests`: Used to make HTTP requests to the PokéAPI and retrieve Pokémon information.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.

## Contribution

Contributions to the project are welcome. If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

Enjoy playing the Pokémon Battle Game!
