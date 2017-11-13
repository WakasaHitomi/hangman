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
    
def play():
    start_screen()
    
    puzzle = get_puzzle()
    guesses = ""
    solved = get_solved(puzzle, guesses)
    display_board(solved, guesses)

    while solved !=  puzzle:
        guesses += get_guess()
        solved = get_solved(puzzle, guesses)
        display_board(solved, guesses)
play()
