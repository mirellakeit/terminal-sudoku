import sys

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


def matrix(lins, cols, val_inic):
    a = [[val_inic] * cols for _ in range(lins)]
    return a


m = matrix(9, 9, ' ')
is_interactive_mode = False
is_batch_mode = False


def fill_position(line, col, value):
    m[line - 1][col] = value


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


invalid_move = False
has_repetition = False
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


delete = False
fill = False
beetween_one_and_eighty = True
counter = 0
first_tips = []
game_progression = []


def test_and_fill_file(move):
    global invalid_move
    global is_batch_mode

    if (move[0] in letters_for_numbers) and (move[1] == ',') and (move[3] == ':') and (1 <= int(move[4]) <= 9):
        fill_position((int(move[2])), letters_for_numbers[move[0]], move[4])
        first_tips.append(f'[{move[0].upper()}][{move[2]}]')
    else:
        print("not ok")
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
    global beetween_one_and_eighty
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
    global beetween_one_and_eighty
    if 1 <= c <= 80:
        beetween_one_and_eighty = False


def check_file(file):
    global beetween_one_and_eighty
    global has_repetition
    global invalid_move
    turn_file_to_matrix(file)
    check_repetition(m)
    check_interval(counter)
    if beetween_one_and_eighty:
        if is_interactive_mode:
            draw(m)
        beetween_one_and_eighty = False
        sys.exit("The number of tips in the file is not beetween the [1, 80] interval.")
    if has_repetition:
        if is_interactive_mode:
            draw(m)
        has_repetition = False
        sys.exit("There are invalid moves within this file.")


# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

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
        print(message_error)
    if invalid_move:
        print(message_error)
    invalid_move = False


# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
def check_batch_move(move):
    global invalid_move
    global first_tips
    move = move.upper().replace(" ", "").replace("\n", "")
    if ',' in move:
        if len(move) == 5:
            move_checker = f'[{move[0]}][{move[2]}]'
            if move_checker in first_tips:
                invalid_move = True
            else:
                test_and_fill_input(move)



def turn_batch_file_to_matrix(file):
    global beetween_one_and_eighty
    global invalid_move
    global counter
    global first_tips
    for given_numbers in file:
        if given_numbers == '\n':
            pass
        else:
            given_numbers = given_numbers.upper().replace(" ", "")
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
        sys.exit("The grid was successfully fulfilled!")
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