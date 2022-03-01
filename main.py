game_board = ["-", "-", "-",
              "-", "-", "-",
              "-", "-", "-"]

"""
    1, 2, 3
    4, 5, 6
    7, 8, 9
"""

available_positions = [0, 1, 2, 3, 4, 5, 6, 7, 8]

active_player = 0

flag = True

winner = None

def isPositionAvailable(pos):
    global available_positions

    for i in available_positions:
        if i == pos:
            available_positions.pop(available_positions.index(i))
            return True
        else:
            continue

    return False

def checkGameOver():
    check_for_winner()

def check_for_winner():
    check_rows()
    check_columns()
    check_diagonals()

def check_rows():
    global flag, game_board, active_player, winner

    row1 = game_board[0] == game_board[1] == game_board[2] != "-"
    row2 = game_board[3] == game_board[4] == game_board[5] != "-"
    row3 = game_board[6] == game_board[7] == game_board[8] != "-"

    if row1 == True or row2 == True or row3 == True:
        flag = False
        if active_player == 0:
            winner = "X"
        else:
            winner = "O"

def check_columns():
    global flag, game_board, active_player, winner

    col1 = game_board[0] == game_board[3] == game_board[6] != "-"
    col2 = game_board[1] == game_board[4] == game_board[7] != "-"
    col3 = game_board[2] == game_board[5] == game_board[8] != "-"

    if col1 == True or col2 == True or col3 == True:
        flag = False
        if active_player == 0:
            winner = "X"
        else:
            winner = "O"

def check_diagonals():
    global flag, game_board, active_player, winner

    dia1 = game_board[0] == game_board[4] == game_board[8] != "-"
    dia2 = game_board[6] == game_board[4] == game_board[2] != "-"

    if dia1 == True or dia2 == True:
        flag = False
        if active_player == 0:
            winner = "X"
        else:
            winner = "O"

def play_game():
    global game_board, active_player, available_positions, flag

    while flag:
        if len(available_positions) == 0:
            flag = False
            continue
        
        if active_player == 0:
            print(f"Player O's turn")
        else:
            print("Player X's turn")

        print(f"{game_board[0]} | {game_board[1]} | {game_board[2]}\n{game_board[3]} | {game_board[4]} | {game_board[5]}\n{game_board[6]} | {game_board[7]} | {game_board[8]}")

        position = int(input("\nChoose a postion from 1-9? ")) - 1
        print()

        if not(isPositionAvailable(position)):
            print("\n*** Enter a valid position ***\n")
            continue

        checkGameOver()

        if active_player == 0:
            game_board[position] = "O"
            active_player = 1
        else:
            game_board[position] = "X"
            active_player = 0

        checkGameOver()
    else:
        print(f"{game_board[0]} | {game_board[1]} | {game_board[2]}\n{game_board[3]} | {game_board[4]} | {game_board[5]}\n{game_board[6]} | {game_board[7]} | {game_board[8]}")
        print(f"Winner is {winner}!!!")

play_game()