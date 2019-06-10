import random

#define function to begin game/ display game menu
def game_menu():
    print("\n")
    print("*"*40)
    print("\n" + '{:^40}'.format("Let's Play") + "\n")
    print("\n" + '{:^40}'.format("Mystery Word"))
    print("\n" + "*"*40 + "\n")
    print('{:^40}'.format("Choose Your Difficulty:"))
    print('{:^40}'.format("1 - Easy"))
    print('{:^40}'.format("2 - Normal"))
    print('{:^40}'.format("3 - Hard"))
    print('{:^40}'.format("4 - Evil Mode >:-|"))
    print("\n")
#While loop keeps running while input stays between 1-4. if anything else is entered, an error message is displayed
    while True:
        difficulty_mode = int(input("Choose 1-4: "))
        if difficulty_mode in range(1,5):
            return difficulty_mode
        else:
            print("Congratulations!, You have entered an invalid input.  Your hard drive will now erase itself.")
    

#get a wordlist for the selected difficulty. 1 = 4-6 letter word list, 2 = 6-8 letter word list, >3 = 8 letters or more
def get_word_list(difficulty_mode, file="words.txt"):
    if difficulty_mode == 1:
        difficulty_range = range(4,7)
    elif difficulty_mode == 2:
        difficulty_range = range(6,9)
    else:
        difficulty_range = range(8,50)

    with open(file, "r") as word_list:
        game_word_list = [
        word.strip().upper()
        for word in list(word_list.readlines())
        if len(word.strip()) in difficulty_range
        ]
    return game_word_list

#select a random word from created word_list
def pick_mystery_word(word_list):
    mystery_word = (random.choice(word_list))
    return mystery_word

#function to input a guess for the selected myster word.  If input is longer than 1 character, print "one at a time"
def input_guess(mystery_word):
    while True:
        guess = input("Guess a letter: ").upper()
        if len(guess) == 1: 
            return guess
        else:
            print("Only one letter at a time!")

#make a list of guesses, that appends each input guess to the list
def make_guess_list(guess):
    while True:
        guess_list.append(guess)
        return guess_list

# conditionally display a letter.  if the letter is already in the list guess_list, then return it.  otherwise return "_"
def display_letter(guess, all_guesses):
    if guess in all_guesses:
        return guess
    else:
        return "_"

#
def print_word(word, guesses):
    output_letters = [display_letter(guess, guesses) for guess in word]
    return(" ".join(output_letters))

def end_game(display_word):
    if "_" in str(display_word):
        return True
    else: 
        print("You Win!")
        return False


if __name__ == "__main__":
    difficulty_mode = game_menu()
    word_list = get_word_list(difficulty_mode)
    mystery_word = pick_mystery_word(word_list)
    letters_in_word = True
    game_session = True
    guess_list = []
    while game_session:
        word = mystery_word
        print(word)
        if letters_in_word:
            print("Your Mystery Word has", len(word), "letters.")
        current_guess = input_guess(mystery_word)
        all_guesses = make_guess_list(current_guess)
        print("Your Guesses:", all_guesses)
        [display_letter(guess, all_guesses) for guess in word]
        display_word = print_word(word, all_guesses)
        print(display_word)
