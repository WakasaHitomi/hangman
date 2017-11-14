#HangMan's_Noose
#Dammorah J.
def start_screen():
    print("   |_______________``\           ▄         ▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄        ▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄       ▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄        ▄  ")
    print("    [/]           [  ]          ▐░▌       ▐░▌▐░░░░░░░░░░░▌▐░░▌      ▐░▌▐░░░░░░░░░░░▌▐░░▌     ▐░░▌▐░░░░░░░░░░░▌▐░░▌      ▐░▌")
    print("    [\]           | ||          ▐░▌       ▐░▌▐░█▀▀▀▀▀▀▀█░▌▐░▌░▌     ▐░▌▐░█▀▀▀▀▀▀▀▀▀ ▐░▌░▌   ▐░▐░▌▐░█▀▀▀▀▀▀▀█░▌▐░▌░▌     ▐░▌ ")
    print("    [/]           |  |          ▐░▌       ▐░▌▐░▌       ▐░▌▐░▌▐░▌    ▐░▌▐░▌          ▐░▌▐░▌ ▐░▌▐░▌▐░▌       ▐░▌▐░▌▐░▌    ▐░▌ ")
    print("    [\]           |  |          ▐░█▄▄▄▄▄▄▄█░▌▐░█▄▄▄▄▄▄▄█░▌▐░▌ ▐░▌   ▐░▌▐░▌ ▄▄▄▄▄▄▄▄ ▐░▌ ▐░▐░▌ ▐░▌▐░█▄▄▄▄▄▄▄█░▌▐░▌ ▐░▌   ▐░▌ ")
    print("    [/]           || |          ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░▌  ▐░▌  ▐░▌▐░▌▐░░░░░░░░▌▐░▌  ▐░▌  ▐░▌▐░░░░░░░░░░░▌▐░▌  ▐░▌  ▐░▌ ")
    print("   [---]          |  |          ▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀█░▌▐░▌   ▐░▌ ▐░▌▐░▌ ▀▀▀▀▀▀█░▌▐░▌   ▀   ▐░▌▐░█▀▀▀▀▀▀▀█░▌▐░▌   ▐░▌ ▐░▌")
    print("   [---]          |@ |          ▐░▌       ▐░▌▐░▌       ▐░▌▐░▌    ▐░▌▐░▌▐░▌       ▐░▌▐░▌       ▐░▌▐░▌       ▐░▌▐░▌    ▐░▌▐░▌ ")
    print("   [---]          |  |          ▐░▌       ▐░▌▐░▌       ▐░▌▐░▌     ▐░▐░▌▐░█▄▄▄▄▄▄▄█░▌▐░▌       ▐░▌▐░▌       ▐░▌▐░▌     ▐░▐░▌")
    print("  oOOOOOo         |  |          ▐░▌       ▐░▌▐░▌       ▐░▌▐░▌      ▐░░▌▐░░░░░░░░░░░▌▐░▌       ▐░▌▐░▌       ▐░▌▐░▌      ▐░░▌ ")
    print(" oOO___OOo        | @|           ▀         ▀  ▀         ▀  ▀        ▀▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀         ▀  ▀         ▀  ▀        ▀▀ ")
    print("oO/|||||\Oo       |  |                            |/|")
    print("OO/|||||\OOo      |  |                            |/| ")
    print("*O\ x x /OO*      |  |                            |/| ")
    print("/*|  c  |O*\      |  |                            |/| ")
    print("   \_O_/    \     |  |                            |/| ")
    print("    \#/     |     |  |                            |/| ")
    print(" |       |  |     | ||                            |/| /¯)")
    print(" |       |  |_____| ||__                          |/|/\/ ")
    print("_/_______\__|  \  ||||  \                         |/|\/")
    print("/___|_|___\_|\  _ | ||\  \                       (¯¯¯) ")
    print("|    |    |\  \//\  \  \  \                      (¯¯¯)")
    print("|    |    | __//  \  \  \  \                     (¯¯¯) ")
    print("|    |    |\|//|\  \  \  \  \                    (¯¯¯)")
    print("------------\--- \  \  \  \  \                   (¯¯¯) ")
    print("\  \  \  \  \  \  \  \  \  \  \                  /¯¯/\ ")
    print("_\__\__\__\__\__\__\__\__\__\__\                / ,^./\ ")
    print("__|__|__|__|__|__|__|__|__|__|__|              / /   \/\ ")
    print("|___| |___|                                   / /     \/\ ")
    print("|###/ \###|                                  ( (       )/) ")
    print("\##/   \##/                                  | |       |/| ")
    print(" ``     ``                                   | |       |/| ")
    print("                                             | |       |/|  ")
    print("                                             ( (       )/) ")
    print("                                              \ \     / / ")
    print("                                               \ `---' / ")
    print("                                                `-----' ")

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

def display_board(solved, guesses):
    print(solved, guesses)

def show_result():
    print("You've Guessed it!")

    while True:
        decision = input("Would you like to play again? (y/n) ")
        decision = decision.lower()

        if decision == 'y' or decision == 'yes':
            return True
        elif descision == 'n' or descision == 'no':
            return False
        else:
            print("You're response was incorrect.")

def play():

    puzzle = get_puzzle()
    guesses = ""
    solved = get_solved(puzzle, guesses)
    display_board(solved, guesses)

    while playing:
        solved !=  puzzle
        guesses += get_guess()
        solved = get_solved(puzzle, guesses)
        display_board(solved, guesses)

        strikes = 0
        limit = 10

        if letter not in puzzle

start_screen()

playing = True

while playing:
    play()

show_results()


