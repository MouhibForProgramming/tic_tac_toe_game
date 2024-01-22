# --------------------------------tic_tac_toe Game---------------------------------------i


# TODO:1 create  the design of the game with | and _
# TODO:2 verify if the first diagonal (i=j)  is homogeneous
# TODO:3 verify if the second diagonal (j=3-1-i)is also homogeneous
# TODO:4 verify each time that the 3 rows has one row is homogeneous also  the same thing for each column


# --------------------------------tic_tac_toe Game---------------------------------------i
import numpy as np

# TODO:1 create  the design of the game with | and _
# TODO:2 verify if the first diagonal (i=j)  is homogeneous
# TODO:3 verify if the second diagonal (j=3-1-i)is also homogeneous
# TODO:4 verify each time that the 3 rows has one row is homogeneous also  the same thing for each column


print("welcome to TIC TAC TOE game.")


def check_equality_row(matrix, row):
    j = 0
    equality = True
    first_item = matrix[row][j]
    for j in range(3):
        if first_item != matrix[row][j]:
            equality = False

    return equality


def equality_column(matrix, column):
    i = 0
    equality = True
    first_item = matrix[i][column]
    for i in range(1, 3):
        if first_item != matrix[i][column]:
            equality = False
    return equality


def check_equality_primary_dig(matrix, colum, row):
    if colum != row:
        return False
    else:
        equality = True
        first_item = matrix[0][0]
        for i in range(1, 3):
            if first_item != matrix[i][i]:
                equality = False

        return equality


def check_matrix_empty_or_not(matrix):
    for row in range(3):
        for column in range(3):
            if matrix[row][column] == "-":
                return False
    return True


def check_secondary_dig(matrix, column, row):
    if column != 3 - row - 1:
        return False
    else:
        equality = True
        first_item = matrix[0][2]
        for i in range(0, 3):
            if matrix[i][3 - i - 1] != first_item:
                equality = False
        return equality


def player_choice():
    player1 = input("choose which sign want you play with:['X','O']: ").upper()
    while player1 not in ["X", "O"]:
        print("invalid choice")
        player1 = input("choose which sign want you play with:['X','O']: ").upper()
    return player1


def game():
    end_of_game = False
    tic_tac_toe = [['-', '-', '-'],
                   ['-', '-', '-'],
                   ['-', '-', '-']
                   ]

    turn = 1
    player1 = player_choice()

    if player1 == "X":
        player2 = "O"
    else:
        player2 = "X"
    players = {player1: "player1", player2: "player2"}
    for row in tic_tac_toe:
        print("|".join(row))

    while not end_of_game:
        try:
            row_number = int(input("pick a row [1,2,3]: "))
            column_number = int(input("pick a column [1,2,3]:"))
        except ValueError:
            print("please enter a number instead of string!!!. ")
            
        else:
            try:
                if tic_tac_toe[row_number - 1][column_number - 1] == "-":
                    if turn % 2 != 0:
                        tic_tac_toe[row_number - 1][column_number - 1] = player1
                    else:
                        tic_tac_toe[row_number - 1][column_number - 1] = player2
                else:
                    print("OOPS.change the cell this cell is not empty.")
                    print("retry the game")
                    break

            except IndexError:
                print("you enter a column or row number not in [1,2,3]!!!!")
                print("please retype the number or row and column 'make sure in range [1,3]'!!")

            else:
                for row in tic_tac_toe:
                    print('|'.join(row))
                turn += 1
                if check_matrix_empty_or_not(tic_tac_toe):
                    end_of_game = True
                    print("Draw!!")
                elif equality_column(tic_tac_toe, column_number - 1):
                    column_of_winner = tic_tac_toe[0][column_number - 1]
                    if player1 == column_of_winner:
                        print(f"{players[player1]} win")
                    else:
                        print(f'{players[player2]} win')
                    end_of_game = True
                    break
                elif check_equality_row(tic_tac_toe, row_number - 1):
                    row_of_winner = tic_tac_toe[row_number - 1][0]
                    if player1 == row_of_winner:
                        print(f"{players[player1]} win")
                    else:
                        print(f'{players[player2]} win')
                    end_of_game = True
                    break
                elif check_equality_primary_dig(tic_tac_toe, column_number - 1, row_number - 1):
                    diagonal_winner = tic_tac_toe[0][0]
                    if player1 == diagonal_winner:
                        print(f"{players[player1]} win")
                    else:
                        print(f'{players[player2]} win')
                    end_of_game = True
                    break
                elif check_secondary_dig(tic_tac_toe, column_number - 1, row_number - 1):
                    diagonal_winner = tic_tac_toe[0][2]
                    if player1 == diagonal_winner:
                        print(f"{players[player1]} win")
                    else:
                        print(f'{players[player2]} win')
                    end_of_game = True
                    break


# run the program as a script instead of imported.
if __name__ == "__main__":
    game()
    while input("do you want to restart the game or not type 'Yes' or 'No': ").title() == "Yes":
        game()
    print("---------------End Of The Game---------------")
    print("---------------See You Later------------------")

# Ai version  of tic tac toe game
