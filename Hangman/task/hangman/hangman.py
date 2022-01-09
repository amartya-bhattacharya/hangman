import random
from random import sample
from nltk.corpus import words
seeds = 100
WORDS = sample(words.words("en-basic"), seeds)


def find(s, ch):
    return [index for index, letter in enumerate(s) if letter == ch]


print("H A N G M A N")
while True:
    mode = input('Type "play" to play the game, "exit" to quit: ')
    if mode == "play":
        choices = [word for word in WORDS if 4 <= len(word) <= 8 and word.islower()]
        print("words:", choices)
        choice = random.choice(choices)
        # print(choice)
        hint = ''
        for i in range(len(choice)):
            hint += "-"
        lives = 8
        tries = []
        while lives > 0:
            print("\n" + hint)
            guess = input("Input a letter: ")
            if len(guess) != 1:
                print("You should input a single letter")
            elif not guess.islower():
                print("Only english letters in lowercase are allowed!")
            elif guess in tries:
                print("You've already guessed this letter")
            elif guess in choice:
                indices = find(choice, guess)
                for i in indices:
                    hint = hint[:i] + guess + hint[i + 1:]
                if hint == choice:
                    print("\n" + hint)
                    print("You guessed the word", hint + "!")
                    print("You survived!\n")
                    break
            else:
                print("That letter doesn't appear in the word")
                lives -= 1
                print("You only have", lives, "lives remaining!")
            tries.append(guess)
        if hint != choice:
            print("You lost!\n")
    elif mode == "exit":
        break
    else:
        continue
