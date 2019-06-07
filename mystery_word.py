import random

#define function to begin game/ display game menu
def game_menu():
    print("\n")
    print("?"*60)
    print("\n" + '{:^60}'.format("Let's Play") + "\n")
    print("\n" + '{:^60}'.format("Mystery Word"))
    print("\n" + "?"*60 + "\n")
    print('{:^60}'.format("Choose Your Difficulty:"))
    print('{:^60}'.format("1 - Easy"))
    print('{:^60}'.format("2 - Normal"))
    print('{:^60}'.format("3 - Hard"))
    print('{:^60}'.format("4 - Evil Mode >:-|"))
    print("\n")
#While loop keeps running while input stays between 1-4. if anything else is entered, an error message is displayed
    while True:
        difficulty_mode = int(input("Choose 1-4: "))
        if difficulty_mode in range(1,5):
            return difficulty_mode
        else:
            print("Congratulations!, You have entered an invalid input.  Your hard drive will now erase itself.")
    
game_menu()

#get a wordlist for the selected difficulty. 1 = 4-6 letter word list, 2 = 6-8 letter word list, >3 = 8 letters or more
def get_word_list(difficulty_mode, file="words.txt"):
    if difficulty_mode == 1:
        difficulty_range = range(4,7)
    elif difficulty_mode == 2:
        difficulty_range = range(6,9)
    else:
        difficulty_range = range(8,50)

    with open(file, "r") as wordlist:
        game_word_list = [
        word.strip().lower()
        for word in list(wordlist)
        if len(word.strip()) in difficulty_range
        ]
    return game_word_list


# difficulty_mode = difficulty_mode
# def pick_mode(difficulty_mode):
#     if difficulty_mode == 1:
#         word_mystery_gamy(file)

