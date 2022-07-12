# terminal-sudoku
 This is my semester's final project in Programming Fundamentals, I just basically have to make a sudoku game on terminal.

Okay, now that the job is done, I can make this repository public so others can see my code and play the game I've done :)

As I said, it is a fully functional sudoku game that runs in terminal, you give a file with the tips in a [1-80] range and then, you play given the tips you've given.
It all happens in your OS' terminal, it does not have a GUI or a interface, so I tried to make the prettiest possible in the terminal itself.

(OBS1: the board is organized like this: The columns are ordered from A to I and the lines are ordered from 1 to 9)
(OBS2: the each move and tip follows the 'COLLUMN,LINE:VALUE' format, for example: 'A,3:8' [in the column A, line 3, the value '8' will be drawn.] it is neither case sensitive nor whitespace sensitive, so plays like 'b,  3 :  7' are also valid.)
(OBS3: for you to delete a space, you use the 'DCOLUMN,LINE' format, for example, the command 'DA,3' will delete any number that is drawn in the collumn A, line 3. Of course, after the tips have been set, you can't delete a place where a tip is.)
(OBS4: If you type a invalid move, the program will promptly ignore it.)

You basically have two gamemodes:

-The first one is the interactive mode. For you to play it, you just go to your terminal, locate the folder where the file 'sudoku.py' is, then, in the same folder, you insert a .txt files with the tips, for example 'tips.txt', then, for you to run, you just have to go in your terminal and type 'python3 sudoku.py tips.txt' or whichever name you choose to your .txt file

In this gamemode, the grid is drawn for you, and you play the game move by move, each move (if valid) will redraw the board and for you to win you basically have to complete the grid (like the usual sudoku.)

-The second one is the batch mode. It works simmilar to the interactive mode, but no boards are drawn, you insert both a 'tips' text file and a 'plays' text file, then, the game will check if you have or have not completed the grid.
For you to play it, you just have to type 'python3 sudoku.py tips.txt plays.txt', like this, you have your .txt file with the tips (which can have whichever name you want) then, you press space and indicate to the programm that it has a .txt with the plays (which can also have whichever name you want). The programm will then now you want batch mode and go forth.

In the github file, I already included a .txt file with the tip and a .txt file with the plays, so you can test it if you want it.

have fun! :)
