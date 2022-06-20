import sys

'''
Well, the lines are arranged from 1 to 9 and the columns are arranged from A to I, henceforth, I will create a dictionary
to correspond each one of these 9 letters to a corresponding number from 0 to 8.
'''
letters_for_numbers = {
    "A": 0,
    "B": 1,
    "C": 2,
    "D": 3,
    "E": 4,
    "F": 5,
    "G": 6,
    "H": 7,
    "I": 8
}

'''
this function creates a matrix with a given number of lines, columns, and a predetermined value at each Aij.
which means, it serves the sole purpose of making my life easier therefront
I will then, create a 9x9 matrix (just like the sudoku board) in which each Aij is a blank space.
'''


def matrix(lins, cols, val_inic):
    a = [[val_inic] * cols for _ in range(lins)]
    return a


m = matrix(9, 9, ' ')

''' 
this is just a simple function to fill a position Aij with given i, j and value.
since the player will input a value from 1 to 9 and the matrix goes from 0 to 8, i will decrease one from the
given line value.
'''

def fill_position(line, col, value):
    m[line - 1][col] = value


'''
now, this function serves two purposes:
1: given a .txt document, the function will read each line from the file and put it to its corresponding matrix position
folowing the 'column,line:value' format.
2: count how many line where there, so it can check if it's beetween the [1, 80] interval. I did this by creating a boolean
beforehand, which is false. If the number of lines is right, the boolean will be true, and the show goes on.
'''

beetween_one_and_eighty = False

def turn_file_to_matrix(f):
    global beetween_one_and_eighty
    counter = 0
    for given_numbers in f:
        given_numbers.strip(" ")
        given_line = int(given_numbers[2])
        given_column = letters_for_numbers[str(given_numbers[0]).upper()]
        given_value = int(given_numbers[4])
        counter += 1

        fill_position(given_line, given_column, given_value)
    if 1 <= counter <= 80:
        beetween_one_and_eighty = True

'''
Then, I created this function, which receives the previous boolean, if this boolean is false, the program will be terminated 
'''

def check_number_of_tips(b):
    if not b:
        sys.exit("The quantity of tips you gave is not between the interval [1, 80]. Try Again")


'''
Now, we gotta check repetitions between a given line, column and square

the functions are pretty straight-foward, it may take some time to understand because you gotta find a proper mathematical 
implementation for the loops, in each one of these three scenarios, but, after quite some time (specialy in the
'check_squares_repetition' one), it all worked out. :)

I also had these three booleans beforehand, 'line_repetition', 'column_repetition' and 'square_repetition' which were all
set to False. If the function finds it true, it will put a "True" value in them.

(I honestly feel like a genius for making these functions, but we can ignore that lol)
'''
line_repetition = False
column_repetition = False
square_repetition = False

def check_line_repetition(m):
    global line_repetition
    line_checker = []
    for x in range(9):
        for y in range(9):
            if m[x][y] != ' ':
                line_checker.append(m[x][y])
        if len(line_checker) != len(set(line_checker)):
            print("there's a repetition in line %d" % (x + 1))
            line_repetition = True
        line_checker = []
    return line_repetition


def check_column_repetition(m):
    global column_repetition
    column_checker = []
    for k in range(9):
        for l in range(9):
            if m[l][k] != ' ':
                column_checker.append(m[l][k])
        if len(column_checker) != len(set(column_checker)):
            print("there's a repetition in column %d" % (k + 1))
            column_repetition = True
        column_checker = []
    return column_repetition


def check_square_repetition(m):
    global square_repetition
    square_checker = []
    for line_multiplier in range(3):
        for col_multiplier in range(3):
            for x in range((3 * line_multiplier), (3 * (line_multiplier + 1))):
                for y in range((3 * col_multiplier), (3 * (col_multiplier + 1))):
                    if m[x][y] != ' ':
                        square_checker.append(m[x][y])
            if len(square_checker) != len(set(square_checker)):
                print("there's a repetition in square %d" % ((col_multiplier + 1) + (3 * line_multiplier)))
                square_repetition = True
            square_checker = []
    return square_repetition



f = open("arq_01_cfg.txt", "r")
turn_file_to_matrix(f)
check_number_of_tips(beetween_one_and_eighty)
f.close()


'''
well, this basicaly just draws the matrix following the format specified in the project.
'''

def draw(m):
    final_matrix = "       A       B       C        D       E       F        G       H       I    \n"
    for i in range(9):
        for j in range(9):
            if j == 0:
                if i % 3 != 0:
                    final_matrix += '  ++-------+-------+-------++-------+-------+-------++-------+-------+-------++\n'
                else:
                    final_matrix += '  ++=======+=======+=======++=======+=======+=======++=======+=======+=======++\n'
                final_matrix += "%s ||   " % (i + 1) + str(m[i][j]) + "   |   "
            elif j == 8:
                final_matrix += str(m[i][j]) + "   || %s\n" % (i + 1)
            elif (j + 1) % 3 == 0:
                final_matrix += str(m[i][j]) + "   "
            elif j % 3 == 0:
                final_matrix += "||   " + str(m[i][j]) + "   |   "
            else:
                final_matrix += str(m[i][j]) + "   |   "

    final_matrix += '  ++=======+=======+=======++=======+=======+=======++=======+=======+=======++\n'
    final_matrix += "       A       B       C        D       E       F        G       H       I    \n"
    print(final_matrix)


'''
who doesn't love functions inside functions huh?
well, I just created a function that encapsulates the three last functions in one. It then, checks if it has repetition
in any of those three cases, assigning it to a boolean called 'has_repetition'. After that, those three booleans I created
previously will be set back to False, so it doesn't interfere in the future, and, in case 'has_repetition' is true, it will
draw the thing and quit the game, with an error message saying 'try again'

the thing is. the 'check_initial_repetition will check if there is a repetition WITHIN the given file.

the 'check_posterior_repetition' will then, check repetitions for each move the player does, which i implemented better
in the main loop.
'''
def check_initial_repetition(m):
    global square_repetition
    global column_repetition
    global line_repetition
    check_line_repetition(m)
    check_column_repetition(m)
    check_square_repetition(m)
    has_repetition = square_repetition or column_repetition or line_repetition
    square_repetition = False
    column_repetition = False
    line_repetition = False

    if has_repetition:
        draw(m)
        sys.exit("Try again.")


check_initial_repetition(m)



def check_posterior_repetition(m):
    global square_repetition
    global column_repetition
    global line_repetition
    global valid_move

    check_line_repetition(m)
    check_column_repetition(m)
    check_square_repetition(m)

    has_repetition = square_repetition or column_repetition or line_repetition

    square_repetition = False
    column_repetition = False
    line_repetition = False

    return has_repetition


'''
well, that's the main loop :)
'''
game_going_on = True

f = open("arq_01_cfg.txt", "r")
turn_file_to_matrix(f)
f.close()
while game_going_on:
    draw(m)
    move = str(input("Type collumn, line, and value you want to input in the format 'column,line:value' "))
    move.strip(" ")

    col = letters_for_numbers[move[0].upper()]
    lin = str(move[2])
    value = str(move[4])

    if m[int(lin) - 1][col] == ' ':
        fill_position(int(lin), int(col), int(value))
        if check_posterior_repetition(m):
            fill_position(int(lin), int(col), ' ')
            print("Please, try again.")
            check_posterior_repetition(m)
    else:
        print("\n\n\n")
        print("You can't put a number where there already is one.")
