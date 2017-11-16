#Cupid's Arrow
#Dammorah J.

limit = 8

def start_screen():
    print("oo      ")
    print("   oo     OOOOOOOO:       OOOOOOOO!        ")
    print("      oOOOO!!!!;;;;O    OO.......:;!O         ")
    print("     'OOO!!!;;;;;;;;O  O.......:   ;!O       ")
    print("     OOO!!!!;;::::::.OO........:    ;!O     ")
    print("     OO!!!!;;:::::..............:   ;!O    ")
    print("    OOO!!!;::::::..............:   ;!O    ")
    print("      OO!!;;::::::.............:   ;!O     ")
    print("      OO!;;::::::......oo.....::::!O       ")
    print("        O!!;::::::........oo..:::O         ")
    print("          !!!;:::::..........ooO           ")
    print("              !!;:::::.......O   oo        ")
    print("               ;;::::.....O        oo  ,o ")
    print("                  :::..O              ooo")
    print("                    ::.              oooo ")
    print("                     :                    ")
    print(" ▄▄▄▄▄▄▄▄▄▄▄  ▄         ▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄  \\  ▄▄▄▄▄▄▄▄▄▄▄       ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄         ▄  ")
    print("▐░░░░░░░░░░░▌▐░▌       ▐░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░▌    ▐░░░░░░░░░░░▌     ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░▌       ▐░▌ ")
    print("▐░█▀▀▀▀▀▀▀▀▀ ▐░▌       ▐░▌▐░█▀▀▀▀▀▀▀█░▌ ▀▀▀▀█░█▀▀▀▀ ▐░█▀▀▀▀▀▀▀█░▌   ▐░█▀▀▀▀▀▀▀▀▀      ▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀█░▌▐░▌       ▐░▌ ")
    print("▐░▌          ▐░▌       ▐░▌▐░▌       ▐░▌     ▐░▌     ▐░▌       ▐░▌   ▐░▌               ▐░▌       ▐░▌▐░▌       ▐░▌▐░▌       ▐░▌▐░▌       ▐░▌▐░▌       ▐░▌")
    print("▐░▌          ▐░▌       ▐░▌▐░█▄▄▄▄▄▄▄█░▌     ▐░▌     ▐░▌       ▐░▌   ▐░█▄▄▄▄▄▄▄▄▄      ▐░█▄▄▄▄▄▄▄█░▌▐░█▄▄▄▄▄▄▄█░▌▐░█▄▄▄▄▄▄▄█░▌▐░▌       ▐░▌▐░▌   ▄   ▐░▌ ")
    print("▐░▌          ▐░▌       ▐░▌▐░░░░░░░░░░░▌     ▐░▌     ▐░▌       ▐░▌   ▐░░░░░░░░░░░▌     ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░▌       ▐░▌▐░▌  ▐░▌  ▐░▌ ")
    print("▐░▌          ▐░▌       ▐░▌▐░█▀▀▀▀▀▀▀▀▀      ▐░▌     ▐░▌       ▐░▌    ▀▀▀▀▀▀▀▀▀█░▌     ▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀█░█▀▀ ▐░█▀▀▀▀█░█▀▀ ▐░▌       ▐░▌▐░▌ ▐░▌░▌ ▐░▌")
    print("▐░▌          ▐░▌       ▐░▌▐░▌               ▐░▌     ▐░▌       ▐░▌             ▐░▌     ▐░▌       ▐░▌▐░▌     ▐░▌  ▐░▌     ▐░▌  ▐░▌       ▐░▌▐░▌▐░▌ ▐░▌▐░▌ ")
    print("▐░█▄▄▄▄▄▄▄▄▄ ▐░█▄▄▄▄▄▄▄█░▌▐░▌           ▄▄▄▄█░█▄▄▄▄ ▐░█▄▄▄▄▄▄▄█░▌    ▄▄▄▄▄▄▄▄▄█░▌     ▐░▌       ▐░▌▐░▌      ▐░▌ ▐░▌      ▐░▌ ▐░█▄▄▄▄▄▄▄█░▌▐░▌░▌   ▐░▐░▌")
    print("▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░▌          ▐░░░░░░░░░░░▌▐░░░░░░░░░░▌    ▐░░░░░░░░░░░▌     ▐░▌       ▐░▌▐░▌       ▐░▌▐░▌       ▐░▌▐░░░░░░░░░░░▌▐░░▌     ▐░░▌")
    print(" ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀            ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀      ▀▀▀▀▀▀▀▀▀▀▀       ▀         ▀  ▀         ▀  ▀         ▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀▀       ▀▀  ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")

def get_puzzle():
    return "velocity"

def get_solved(puzzle, guesses):
    solved = ""

    for letter in puzzle:
        if letter in guesses:
            solved += letter
        else:
            solved += "-"

    return solved

def get_guess():
    letter = input ("Guess a letter")
    letter = letter.lower()
    return letter

def show_credits():
    print("Origial base for Hangman game...... J. Cooper")
    print(" ")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print(" ")
    print("      __   __       ")
    print("     /  \./  \/\_                              ")
    print("  __{^\_ _}_   )  }/^\                              ")
    print(" /  /\_/^\._}_/  //  /                             ")                      
    print("(  (__{(@)}\__}.//_/__A____A_______A________A________A_____A___A___A_____ ")
    print(" \__/{/(_)\_}  )\\ \\---v-----V-----V---Y-----v----Y------v-----V-----v-- ")
    print("   (   (__)_)_/  )\ \>    ")
    print("    \__/     \__/\/\/ ")
    print("       \__,--'     ")
    print(" ")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print(" ")
    print("Modified and Recreated by........WakasaHitomi")

def display_board(solved, guesses):
    print(solved, guesses)

def show_result(strikes, limit):
    if strikes <= limit:
        print("You've Guessed it!")

    if strikes > limit:
        print("You have taken an L. Good try though.")

    while True:
        decision = input("Would you like to play again? (y/n) ")
        decision = decision.lower()

        if decision == 'y' or decision == 'yes':
            return True
        elif decision == 'n' or decision == 'no':
            show_credits()
        else:
            print("You're response was incorrect.")

def mistakes(strikes, limit):
    if strikes == 0:
        print(",d88b.d88b,  ,d88b.d88b, ,d88b.d88b, ,d88b.d88b, ,d88b.d88b,  ,d88b.d88b,  ,d88b.d88b,  ,d88b.d88b,     ")
        print("88888888888  88888888888 88888888888 88888888888 88888888888  88888888888  88888888888  88888888888  ")
        print("`Y8888888Y'  `Y8888888Y' `Y8888888Y' `Y8888888Y' `Y8888888Y'  `Y8888888Y'  `Y8888888Y'  `Y8888888Y' ")
        print("  `Y888Y'      `Y888Y'     `Y888Y'     `Y888Y'     `Y888Y'      `Y888Y'      `Y888Y'      `Y888Y'  ")
        print("    `Y'          `Y'         `Y'         `Y'         `Y'          `Y'          `Y'          `Y'  ")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~ " + str(limit) + "strikes left ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~" + str(strikes) + "wrong guesses ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        
    if strikes == 1:
        print(",d88b.d88b,  ,d88b.d88b, ,d88b.d88b, ,d88b.d88b, ,d88b.d88b,  ,d88b.d88b,  ,d88b.d88b, |,d88b/ /d88b,     ")
        print("88888888888  88888888888 88888888888 88888888888 88888888888  88888888888  88888888888 |88888\ \88888  ")
        print("`Y8888888Y'  `Y8888888Y' `Y8888888Y' `Y8888888Y' `Y8888888Y'  `Y8888888Y'  `Y8888888Y' |`Y888/ /888Y' ")
        print("  `Y888Y'      `Y888Y'     `Y888Y'     `Y888Y'     `Y888Y'      `Y888Y'      `Y888Y'   |  `Y8\ \8Y'  ")
        print("    `Y'          `Y'         `Y'         `Y'         `Y'          `Y'          `Y'     |     `Y'  ")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~ " + str(limit) + "strikes left ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~" + str(strikes) + "wrong guesses ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

        '''
    if strikes == 2:
	print(",d88b.d88b,  ,d88b.d88b, ,d88b.d88b, ,d88b.d88b, ,d88b.d88b,  ,d88b.d88b,  |,d88b/ /d88b,   ,d88b/ /d88b,  ")
	print("88888888888  88888888888 88888888888 88888888888 88888888888  88888888888  |88888\ \88888   88888\ \88888 ")
	print("`Y8888888Y'  `Y8888888Y' `Y8888888Y' `Y8888888Y' `Y8888888Y'  `Y8888888Y'  |`Y888/ /888Y'   `Y888/ /888Y' ")
	print("  `Y888Y'      `Y888Y'     `Y888Y'     `Y888Y'     `Y888Y'      `Y888Y'    |  `Y8\ \8Y'       `Y8\ \8Y'")
	print("    `Y'          `Y'         `Y'         `Y'         `Y'          `Y'      |     `Y'             `Y'   ")
	print("~~~~~~~~~~~~~~~~~~~~~~~~~~~ " + str(limit) + "strikes left ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
	print("~~~~~~~~~~~~~~~~~~~~~~~~~~~" + str(strikes) + "wrong guesses ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    if strikes == 3:
	print(",d88b.d88b,  ,d88b.d88b, ,d88b.d88b, ,d88b.d88b, ,d88b.d88b,  |,d88b/ /d88b,   ,d88b/ /d88b, ,d88b/ /d88b, ")
	print("88888888888  88888888888 88888888888 88888888888 88888888888  |88888\ \88888   88888\ \88888 88888\ \88888")
	print("`Y8888888Y'  `Y8888888Y' `Y8888888Y' `Y8888888Y' `Y8888888Y'  |`Y888/ /888Y'   `Y888/ /888Y' `Y888/ /888Y' ")
	print("  `Y888Y'      `Y888Y'     `Y888Y'     `Y888Y'     `Y888Y'    |  `Y8\ \8Y'       `Y8\ \8Y'     `Y8\ \8Y' ")
	print("    `Y'          `Y'         `Y'         `Y'         `Y'      |     `Y'             `Y'           `Y' ")
	print("~~~~~~~~~~~~~~~~~~~~~~~~~~~ " + str(limit) + "strikes left ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
	print("~~~~~~~~~~~~~~~~~~~~~~~~~~~" + str(strikes) + "wrong guesses ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
	'''
	
def play():
    strikes = 0
    
    puzzle = get_puzzle()
    guesses = ""
    solved = get_solved(puzzle, guesses)
    display_board(solved, guesses)

    while playing:
        solved !=  puzzle
        guesses += get_guess()
        solved = get_solved(puzzle, guesses)
        display_board(solved, guesses)
        
        if guesses not in puzzle:
            strikes += 1

        mistakes()

        if strikes > limit:
            show_result(strikes, limit)

        if puzzle == solved:
            show_result(strikes, limit)

start_screen()

playing = True

while playing:
    play()
    playing = play_again()

show_result(strikes, limit)
