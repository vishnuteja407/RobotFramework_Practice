def display_board(board):
    print(" | | ")
    print(board[1] + "|" + board[2] + "|" + board[3])
    print(" | | ")
    print("------")
    print(" | | ")
    print(board[4] + "|" + board[5] + "|" + board[6])
    print(" | | ")
    print("------")
    print(" | | ")
    print(board[7] + "|" + board[8] + "|" + board[9])
    print(" | | ")


# display_board(test_board)

def game_position():
    player_data = " "
    while player_data not in range(1, 10):
        player_data = input("Enter a position(1 to 9): ")

        if player_data not in range(1, 10):
            print("Sorry, Please enter correct value!")

def player_input():
    marker = ""
    while marker != 'X' and marker != "O":
        marker = input("Player 1, choose X or O: ").upper()
    player1 = marker
    if player1 == 'X':
        player2 = 'O'
    else:
        player2 = "X"

    return (player1, player2)

# display_board(test_board)
# def place_marker(test_board, marker, position):
#     marker = marker
#     while marker not in ["O", "X"]:
#         print("Invalid marker, enter X or O")
#         marker = input("Enter marker X or O: ")
#         if marker == "X" or marker == "O":
#             test_board[position] = marker
def place_marker(test_board, marker, position):
    test_board[position] = marker

def win_check(board, mark):
    return ((board[1] == board[2] == board[3] == mark) or (board[4] == board[5] == board[3] == mark)
            or (board[7] == board[8] == board[9] == mark) or (board[1] == board[4] == board[7] == mark)
            or (board[2] == board[5] == board[8] == mark) or (board[3] == board[6] == board[9] == mark)
            or (board[1] == board[5] == board[9] == mark) or (board[3] == board[5] == board[7] == mark))

import random
def choose_first():
    flip = random.randint(0, 1)
    if flip == 0:
        return "Player 1"
    else:
        return "Player 2"

def space_check(board, position):
    return board[position] == " "

def full_board_check(board):
    for i in range(1, len(board)):
        return board[i] != " "

# print(full_board_check(test_board))

def player_choice(board):
    position = 0
    while position not in range(1, len(board)) or not space_check(board, position):
        position = int(input("Enter a position (1 to 9): "))
    return position

def replay():
    choice = input("Play again? Enter Yes or No")
    return choice.lower() == "yes"

while True:
    test_board = [" "] * 10
    player1_marker, player2_marker = player_input()

    turn = choose_first()
    print(turn+" will go first")

    play_game = input("Ready to Play: y or n")

    if play_game == 'y':
        game_on = True
    else:
        game_on = False

    while game_on:
        if turn == "Player 1":
            display_board(test_board)
            position = player_choice(test_board)
            place_marker(test_board, player1_marker, position)
            if win_check(test_board, player1_marker):
                display_board(test_board)
                print("PLAYER 1 HAS WON!!!")
                game_on = False
            else:
                if full_board_check(test_board):
                    display_board(test_board)
                    print("TIE Game!!!")
                    game_on = False
                else:
                    turn == "Player 2"
        else:
            if turn == "Player 2":
                display_board(test_board)
                position = player_choice(test_board)
                place_marker(test_board, player2_marker, position)
                if win_check(test_board, player2_marker):
                    display_board(test_board)
                    print("PLAYER 2 HAS WON!!!")
                    game_on = False
                else:
                    if full_board_check(test_board):
                        display_board(test_board)
                        print("TIE Game!!!")
                        game_on = False
                    else:
                        turn == "Player 1"


    if not replay():
        break



