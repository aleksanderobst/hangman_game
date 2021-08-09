import random
import string


def game():
    guess_list = ['python', 'java', 'kotlin', 'javascript']
    random_name = random.choice(guess_list)
    lives = 8
    display_list = []
    tried_list = []
    alphabet = string.ascii_lowercase
    for i in range(len(random_name)):
        display_list.append("-")

    while lives > 0:
        print()
        print(''.join(display_list))
        word_temp = ''.join(display_list)
        tried = ''.join(tried_list)

        if word_temp == random_name:
            print("You guessed the word!")
            print("You survived!")
            break

        input_user = input("Input a letter: ")
        if len(input_user) != 1:
            print('You should input a single letter')
        elif input_user in tried:
            print("You've already guessed this letter")
        elif input_user not in alphabet:
            print("Please enter a lowercase English letter")

        else:
            if input_user in random_name:
                for i in range(len(random_name)):
                    if input_user == random_name[i]:
                        display_list[i] = input_user
                tried_list.append(input_user)
            elif input_user not in random_name:
                print("That letter doesn't appear in the word")
                lives -= 1
                if lives == 0:
                    print('You lost!')
                tried_list.append(input_user)


print('H A N G M A N')
while True:
    menu = input('Type "play" to play the game, "exit" to quit: ')
    if menu == "play":
        game()
    elif menu == "exit":
        break
