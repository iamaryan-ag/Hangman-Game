# Hangman Game
import random

def letter(curr, word, guess, wrong_letters):
    flag=0
    curr_new=""
    for i in range(len(word)):
        if word[i]==guess:
            curr_new=curr_new+guess
            flag=1
        else: 
            curr_new=curr_new+curr[i]
    if flag==0:
        wrong_letters.append(guess)
    print(2)
    return(curr_new, wrong_letters)



# Selecting word for Hangman Game
with open("wordlist.txt","r") as filein:
    wordlist=filein.readlines()

word=wordlist[random.randrange(len(wordlist))].strip()

print("Number of letters in word is: ", len(word))
print("_ "*len(word))
print()
print(word)

tries=1
max_tries=7
flag=0
wrong_letters=[]
curr="_"*len(word)

while tries!=max_tries:
    print("Try number: ", tries)
    print("Current progress: ", curr)
    print("Wrong letters entered: ")
    print()
    for i in wrong_letters: print(i, end=',')

    guess=input("Guess word or letters present in the word: ")
    print()
    
    if guess.isalpha():

        if len(guess)==1:
            if guess in word and guess not in curr:
                curr, wrong_letters=letter(curr, word, guess, wrong_letters)
            
            if guess not in word:
                tries+=1
            
            if curr==word:
                print("Correct! The word is: ", word)
                flag=1
                break
            

        elif len(guess)>1:
            if guess==word: 
                print("Correct!")
                flag=1
                break
            else:
                print("Incorrect!")
                tries+=1

if flag==0: print("You lost the game. Try again next time!")
