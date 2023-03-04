N Queens Puzzle
The N Queens Puzzle is a classic problem in computer science that challenges the player to place N non-attacking queens on an N x N chessboard. The problem can be solved using various algorithms, with the backtracking algorithm being one of the most popular methods.

This program solves the N Queens Puzzle using the backtracking algorithm. It takes an integer N as a command-line argument, generates all possible solutions to the problem, and prints them to the console.

Requirements
Python 3.x
Usage
Run the program by executing the following command in the terminal:

Copy code
python nqueens.py N
Where N is an integer value greater than or equal to 4. The program will generate and print all possible solutions to the N Queens Puzzle with one solution per line.

If the user calls the program with the wrong number of arguments, the program will print a usage message and exit with status 1. If N is not an integer or is smaller than 4, the program will print an error message and exit with status 1.
