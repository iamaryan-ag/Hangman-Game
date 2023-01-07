import random

# Selecting word for Hangman Game
with open("wordlist.txt","r") as filein:
    lines = sum(1 for line in filein)
    filein.seek(0)
    for j in range(random.randrange(lines)):
        filein.readline()
    word = filein.readline().strip()

print("Number of letters in word is: ", len(word))
print("_ "*len(word))

tries = 1
max_tries = 7
wrong_letters = ""
curr = ["_"] * len(word)

while True:
    print("\nTry number: ", tries)
    print("Current progress: ", " ".join(curr))
    print("Wrong letters entered: ", wrong_letters)

    guess = input("\nGuess word or letters present in the word: ")

    if guess.isalpha():
        if len(guess) == 1:
            if guess in word:
                for i in range(len(word)):
                    if word[i] == guess:
                        curr[i] = guess
            elif guess not in word and guess not in wrong_letters:
                wrong_letters += guess
                tries += 1
            
            if "".join(curr) == word:
                print("Correct! The word is: ", word)
                break
        elif len(guess) > 1:
            if guess == word: 
                print("Correct!")
                break
            else:
                print("Incorrect!")
                tries += 1

    if tries == max_tries:
        print("You lost the game. Try again next time!")
        print("The word was: ", word)
        break
