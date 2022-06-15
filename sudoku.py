letters_for_numbers = {
    "A": 0,  # Well, the lines are arranged from 1 to 9, and the collumns are arranged from A to I,
    "B": 1,  # I just created a dictionary to correspond each one of these 9 letters to a corresponding
    "C": 2,  # number from 0 to 8.
    "D": 3,
    "E": 4,
    "F": 5,
    "G": 6,
    "H": 7,
    "I": 8
}


def matrix(lins, cols, val_inic):  # This function creates a matrix with a given number of lines, collumns,
    a = [[val_inic] * cols for _ in range(lins)]  # and a predetermined initial value at each Aij, which means it serves
    return a  # the sole purpuose of making my life easier therefront.


m = matrix(9, 9, ' ')  # The main Matrix.


def fill_position(line, col, value):  # Just a simple function to fill a position Aij with a given value.
    m[line - 1][col] = value  # Since the player will input a value from 1 to 9 and the matrix goes from
    # 0 to 8, I will decrease one from the given line value.


# The initial position filled are made from that.
def turn_file_to_matrix(f):
    for given_numbers in f:
        given_numbers.strip(" ")
        given_line = int(given_numbers[2])  # Just working the files initial positions filled
        given_column = letters_for_numbers[str(given_numbers[0]).upper()]  # through the Sudoku board.
        given_value = int(given_numbers[4])

        fill_position(given_line, given_column, given_value)


f = open("python3 sudoku.py arq_01_cfg.txt", "r")
turn_file_to_matrix(f)
f.close()


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


#main loop:
game_going_on = True
valid_move = True
f = open("python3 sudoku.py arq_01_cfg.txt", "r")
turn_file_to_matrix(f)
f.close()
while game_going_on:
    draw(m)
    move = str(input("Type collumn, line, and value you want to input in the format 'column,line:value' "))
    move.strip(" ")

    col = letters_for_numbers[move[0].upper()]
    lin = str(move[2])
    value = str(move[4])

    fill_position(int(lin), int(col), int(value))


