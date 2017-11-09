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
    return letter

def display_board(solved):
    print(solved)

def show_result():
    print("You've Guessed it!")
    
def play():
    puzzle = get_puzzle()
    guesses = ""

    guesses += get_guess()
    solved = get_solved(puzzle, guesses)
    display_board(solved)
play()
