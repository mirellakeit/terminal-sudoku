import sys

# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
'''
PART ONE: general functions
I'm an OOP programmer and, even though I didn't use those kinds of stuff in this project (since it was required not to),
I couldn't help but organize it in my brain in a shady OOP-kinda way.

So this first part here of the code are from functions, dictionaries and variables that'll be used throughout the whole
gameplay, It doesn't matter if it's interactive mode, batch mode, a file's tip or a player's input.


'''

'''
First of all, I created a Dictionary that will later be used, since, for the player, the collumns grind will have, for
the player the format 'a,b,c,d,e,f,g,h,i'
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
Then, Since matrix's in Python are no more than a list of lists, I created a 'matrix' function to create this list of lists
(a.k.a. matrix) and then proceeded to create the matrix 'm', which will be our game's main matrix, with size 9x9 and all
its values initially filled with a blank space.

I then, created the function 'fill_position' that will, fill the value 'value' in the 'm' matrix at a given line 
(line - 1 since the player's input will be from 1 to 9 and in python the lists are from 0 to 8) and collumn col.
'''


def matrix(lins, cols, val_inic):
    a = [[val_inic] * cols for _ in range(lins)]
    return a


m = matrix(9, 9, ' ')


def fill_position(line, col, value):
    m[line - 1][col] = value


'''
the 'draw' function seems a little big and hard to understand but it serves the sole purpose of drawing the matrix, that's
it :)
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
Okay, so here are the variables! Well, they're all booleans here
those variables here will be useful to check therefront some stuff, let me explain: 

'Is_interactive_mode' and 'is_batch_mode' serve to indicate wheter we're playing interactive or batch mode.

'line_repetition', 'column_repetition' and 'square_repetition' are pretty self-explanatory, they'll check if there are 
repetetitions in a line, column or square, respectively.

'has_repetition' will later be used as to encapsulate those three prior booleans. I preset it as 'has_repetition = False'
instead of 'has_repetition = line_repetition or square_repetition or square_repetition' because I'll only check those
other three in the future, and I want to have better control of whether 'has_repetition' is True or False

And, finally, 'invalid_move' is probably the one that'll pop up the most later on, it serves the sole purpose to 
tell whether a move is or isn't invalid :)
'''
is_interactive_mode = False
is_batch_mode = False
line_repetition = False
column_repetition = False
square_repetition = False
has_repetition = False
invalid_move = False

'''
okay, the four repetition checker functions:
'check_line_repetition()', 'check_column_repetition()' and 'check_square_repetition'
those, using some matrix math and mathematical pattern recognition, will se if a given number is or isn't repeated in 
a given line, column or square, of a matrix respectively :)

the 'check_repetition()' will encapsulate 'em all, and atribute the value 'line_repetition or column repetition or square_
repetition' to the 'has_repetition' variable.

I also implemented error messages that warns the player where the repetition is.

'''


def check_line_repetition(m):
    global line_repetition
    line_checker = []
    for x in range(9):
        for y in range(9):
            if m[x][y] != ' ':
                line_checker.append(m[x][y])
        if len(line_checker) != len(set(line_checker)):
            if is_interactive_mode:
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
            if is_interactive_mode:
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


def check_repetition(m):
    global has_repetition
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


# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
'''
PART TWO: handling the tips file.

So, now that all the general functions and variables are set, let's work in particular cases.
First thing is the main tips file.

But, before that, there are some variables and functions that will be used later on, not just on the main file.
The variables 'delete' and 'fill' will actually be used to check whether a given command was a 'fill' command or a 'delete'
command

'counter' will be used to count the number of tips and 'between_one_and_eighty' will be used to check whether or not
the number of tips in the main file is in the [1, 80] interval
 
then, I created the list 'first_tips' which will store the given tips and the list 'game_progression' which will store
the player's moves.
'''

delete = False
fill = False
counter = 0
between_one_and_eighty = True
first_tips = []
game_progression = []

'''
Ok, since Python follows a line order, the functions will be better explained in a reverse order.

The function 'check_file()' will check the file, and the tips in it.
It will then call the 'turn_file_to_matrix()' function, which will format each tip on each line and call the
'format_file_test_and_play()' function, which will check if the given tip is correctly typed, and wheter it is a 
'fill' move or a 'delete' move, given the number of characters the string has.
If it is a 'delete' move, it will cal the 'test_and_delete()' function, which deletes a given value in a given 
position in the matrix. This last function has some 'try' and 'except' to check if the given cell is or isn't already
blank.

And, finally, The 'test_and_fill_file()' function will fill the given values in all of the given matrix's positions.

Coming back to the 'check_file_function()' after all of this road to check the file, it will draw our sudoku board, 
if everything is on point.

It will then, append all of the given tips to the 'first_tips' list.

of course, all those last functions I just talked about are full of 'checkers' to see if the function has some repetition,
follows a predetermined format and so on. If so, the game will continue, if not, the 'invalid_move' boolean will be True
and it will unchain some error messages.
'''


def test_and_fill_file(move):
    global invalid_move
    global is_batch_mode

    if (move[0] in letters_for_numbers) and (move[1] == ',') and (move[3] == ':') and (1 <= int(move[4]) <= 9):
        fill_position((int(move[2])), letters_for_numbers[move[0]], move[4])
        first_tips.append(f'[{move[0].upper()}][{move[2]}]')
    else:
        if is_batch_mode:
            print('The move %s is invalid' % f'({move[0]},{move[2]}) = {move[4]}')
        invalid_move = True


def test_and_delete(move):
    global invalid_move
    global counter
    global game_progression
    move = move.upper()
    move_as_a_string = f'[{move[1]}][{move[3]}]'
    if (move[0] == 'D') and (move[2] == ',') and (move[1] in letters_for_numbers):
        fill_position((int(move[3])), letters_for_numbers[move[1]], ' ')

        try:
            if move_as_a_string in game_progression:
                game_progression.remove(move_as_a_string)
            else:
                first_tips.remove(move_as_a_string)
            counter -= 1
        except ValueError:
            print("This cell already has nothing in it!")
    else:
        invalid_move = True


def format_file_test_and_play(move):
    global invalid_move
    move = move.replace(" ", "").replace("\n", "").upper()

    if ',' in move:
        if len(move) == 5:
            test_and_fill_file(move)
        if len(move) == 4:
            test_and_delete(move)
    else:
        invalid_move = True


def turn_file_to_matrix(file):
    global between_one_and_eighty
    global invalid_move
    global counter
    global first_tips
    for given_numbers in file:
        if given_numbers == '\n':
            pass
        else:
            given_numbers = given_numbers.upper().replace(" ", "")
            format_file_test_and_play(given_numbers)
            if invalid_move:
                print('The move %s is invalid' % given_numbers)
            invalid_move = False
            counter += 1


def check_interval(c):
    global between_one_and_eighty
    if 1 <= c <= 80:
        between_one_and_eighty = False


def check_file(file):
    global between_one_and_eighty
    global has_repetition
    global invalid_move
    turn_file_to_matrix(file)
    check_repetition(m)
    check_interval(counter)
    if between_one_and_eighty:
        if is_interactive_mode:
            draw(m)
        between_one_and_eighty = False
        sys.exit("The number of tips in the file is not beetween the [1, 80] interval.")
    if has_repetition:
        if is_interactive_mode:
            draw(m)
        has_repetition = False
        sys.exit("There are invalid moves within this file.")


# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
'''
PART THREE: time for the player

Okay, so now I designed those functions below to be used in interactive mode. But some of them could be and were used
in batch mode.

Now, let's go, in reverse order:
THe 'interactive_mode()' function is the function that will do everything once interactive mode is selected.
Since interactive mode works as a game with subsequent moves, it will work on a loop, so while the game is running,
the function will repeat.
Okay, firstly, the board will be drawn, a player's input will be asked and then, given the input, the function will call

the 'play()' function which serves to call the 'check_input()' function, which is a function that checks if the given
input is valid. If not, the boolean 'invalid_move' will be turned to true, which, in the will be used in the 'play()'
function to print a message saying that the given move is invalid. It'll also use a 'try' and 'except' in the case of a 
player entering a completely nonsensical input.

Finally, the 'test_and_fill_input()' function works simmilarly to the 'test_and_fill_file()' function, which will 
see if everything is good with the player's input, in which case, the move will be made. If not, invalid_move will be true. 

Also, now I'm starting to work with the 'game_progression' list. After each subsequent valid move, the player's move will
be added to the list, and, if a player deletes the move, or makes a invalid move that erases a move from beforehand, the 
move will be deleted from the list.

when the length of set(game_progression) + the length of set(first_tips) = 81, each means that the game was won.
[OBS: set() is a list that ignores all of the repetitions.]
'''


def test_and_fill_input(move):
    global invalid_move
    global game_progression
    global has_repetition
    move_as_a_string = f'[{move[0]}][{move[2]}]'
    if (move[0] in letters_for_numbers) and (move[1] == ',') and (move[3] == ':') and (1 <= int(move[4]) <= 9):
        fill_position((int(move[2])), letters_for_numbers[move[0]], move[4])
        check_repetition(m)
        if has_repetition:
            fill_position(int(move[2]), letters_for_numbers[move[0]], " ")
            invalid_move = True
            if move_as_a_string in game_progression:
                game_progression.remove(move_as_a_string)
        else:
            game_progression.append(move_as_a_string)
    else:
        invalid_move = True


def check_input(move):
    global invalid_move
    global first_tips
    move = move.replace(" ", "").upper()
    if ',' in move:
        if len(move) == 5:
            move_checker = f'[{move[0]}][{move[2]}]'
            if move_checker in first_tips:
                print("You can't place a number where a tip is already.")
            else:
                test_and_fill_input(move)

        elif len(move) == 4:
            move_checker = f'[{move[1]}][{move[3]}]'
            if move_checker in first_tips:
                print("You can't delete a place where a tip is.")
            else:
                test_and_delete(move)
        else:
            invalid_move = True
    else:
        invalid_move = True


def play(move):
    move = move.upper()
    global invalid_move
    message_error = ("the move %s is not a valid move" % move)
    try:
        check_input(move)
    except ValueError:
        invalid_move = True
    if invalid_move:
        print(message_error)
    invalid_move = False


def interactive_mode():
    global first_tips
    global game_progression
    global first_tips
    global is_interactive_mode
    is_interactive_mode = True
    is_running = True
    while is_running:
        draw(m)
        print(game_progression)
        players_move = input("Please, enter your move: ")
        play(players_move)

        if (len(set(first_tips)) + len(set(game_progression))) == 81:
            draw(m)
            is_running = False
    sys.exit("Congratulations, You have won the game!!!!")


# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
'''
PART FOUR: batch baby!!

OK, now, batch mode.
You know the drill, reverse order, let's go:

The 'batch_mode()' function will open a given file, with the player's moves, it will then call the
'turn_batch_file_to_matrix()' function, that formats each move in each line and calls the
'check_batch_move()' function, which will then proceed to call the before mentioned 'test_and_fill_input()' which will then
proceed to check each move just like in the interactive mode. The main difference is that, in batch mode, it all happens
instantly (a.k.a. depending on the time the computer processes all of it) and no drawns are made.

then, it will print error messages, showing where are some invalid moves, tell the player whether of not the grid has 
been fullfiled and end the game.

'''


def check_batch_move(move):
    global invalid_move
    global first_tips
    if ',' in move:
        if len(move) == 5:
            move_checker = f'[{move[0]}][{move[2]}]'
            if move_checker in first_tips:
                invalid_move = True
            else:
                test_and_fill_input(move)


def turn_batch_file_to_matrix(file):
    global between_one_and_eighty
    global invalid_move
    global counter
    global first_tips
    for given_numbers in file:
        if given_numbers == '\n':
            pass
        else:
            given_numbers = given_numbers.upper().replace(" ", "").replace("\n", "")
            check_batch_move(given_numbers)
            if invalid_move:
                print('The move %s is invalid' % f'({given_numbers[0]},{given_numbers[2]}) = {given_numbers[4]}')
            invalid_move = False


def batch_mode(f):
    global is_batch_mode
    global game_progression
    global first_tips
    is_batch_mode = True
    file = open(f, 'r')
    turn_batch_file_to_matrix(file)
    file.close()

    if len(set(first_tips)) + len(set(game_progression)) == 81:
        sys.exit("Congratulations! The grid was successfully fulfilled!! \o/")
    sys.exit("The grid has NOT been fulfilled :(")


def interactive_mode():
    global first_tips
    global game_progression
    global first_tips
    global is_interactive_mode
    is_interactive_mode = True
    is_running = True
    while is_running:
        draw(m)
        players_move = input("Please, enter your move: ")
        play(players_move)

        if (len(set(first_tips)) + len(set(game_progression))) == 81:
            draw(m)
            is_running = False
    sys.exit("Congratulations, You have won the game!!!!")


# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
'''
PART FIVE: main

Now, the only thing left to do is to have the main loop, in which, depending on the given sys.argv given in the terminal
will initialize the interactive or the batch mode, it will then play. and that's it.

Phew, that was a mouthful! 
'''


def main():
    f = open(sys.argv[1], 'r')
    check_file(f)
    f.close()
    if len(sys.argv) == 2:
        interactive_mode()
    elif len(sys.argv) == 3:
        batch_mode(sys.argv[2])


if __name__ == '__main__':
    main()
