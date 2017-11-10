#HangMan's_Noose
#Dammorah J.

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
    puzzle = get_puzzle()
    guesses = ""
    solved = get_solved(puzzle, guesses)
    display_board(solved, guesses)

    while solved !=  puzzle:
        guesses += get_guess()
        solved = get_solved(puzzle, guesses)
        display_board(solved, guesses)
play()
