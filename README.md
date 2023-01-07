Hangman Game
Hangman is a classic word guessing game in which the player has to guess a word by suggesting letters or numbers, within a certain number of tries.
The game is won if the player guesses the word correctly before the number of tries is exceeded.

How to play
1. The program will select a random word from a list of words and display the number of letters in the word.
2. The player will be asked to guess a letter or a word.
3. If the player guesses a correct letter that is present in the word, the letter will be revealed in its correct position(s) in the word.
4. If the player guesses a wrong letter or an incorrect word, the number of tries will be reduced by one.
5. The player wins if they correctly guess the word before the number of tries is exceeded.

Requirements
Python 3.x

Running the game
1. Clone or download the repository.
2. Navigate to the directory where the game is stored.
3. Run the game using the following command: python hangman.py

File structure
hangman.py: The main file that contains the game logic.
wordlist.txt: A list of words from which the game will select a random word.
