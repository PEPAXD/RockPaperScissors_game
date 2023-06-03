# Rock Paper Scissors Game

This is a simple command-line implementation of the popular game Rock Paper Scissors. The user can play against the computer and see who wins.

## Requirements
- Python 3.x

## Usage
1. Clone or download the repository.
2. Navigate to the directory containing the code files.
3. Open a terminal or command prompt in that directory.
4. Run the following command to start the game:
5. Follow the instructions on the screen to choose your option (rock, paper, or scissors).
6. The computer will randomly select its option.
7. The winner will be displayed on the screen.
8. You will be asked if you want to play again. Enter 'y' to play again or 'n' to exit the game.

## Code Explanation
The code consists of several functions:

- `userInput()`: This function prompts the user to choose their option and returns both the user's and computer's choices.
- `checkWinner(computer_input, user_input)`: This function compares the user's and computer's choices and determines the winner.
- `playAgain()`: This function asks the user if they want to play again and restarts the game if they choose to continue.
- `main()`: This function is the entry point of the program. It calls the `userInput()`, `checkWinner()`, and `playAgain()` functions to run the game.

The program uses the `random` module to generate a random choice for the computer. The user's input is taken from the command line using `input()`.

After each game, the screen is cleared using the `os.system("cls")` command (Windows) to provide a cleaner user interface.

## License
This project is licensed under the [MIT License](LICENSE).

Feel free to modify and distribute the code as per the terms of the license.

## Contributing
Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

## Author
This Rock Paper Scissors game was created by [MAURO PEPA].

