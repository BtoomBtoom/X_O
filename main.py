#viriable
player_1_mark = ''
player_2_mark = ''

board = [' ',' ',' ',' ',' ',' ']
index = []
in_put = ''

#welcome
def welcome():
    input_1 = ''
    input_2 = ''
    while input_1 not in ['X', 'O']:
        input_1 = (input("PLayer 1 choose: X or O: ")).upper()
    if input_1 == 'X':
        input_2 = 'O'
    elif input_1 == 'O':
        input_2 = 'X'
    return input_1,input_2


#check in_put, choose player
def input_check(index):
    check = False
    in_put = ""

    while not check:
        in_put = ""
        while in_put not in ['1','2','3','4','5','6','7','8','9']:
            in_put = input("Where do you want to play? 1-9: ")
        if in_put not in index:
            index.append(in_put)
            check = True
        else:
            print("already taken, pick another")
    return int(in_put)
#update board
def update_board_player_1(in_put,board,player_1_mark):
    board[in_put-1] = player_1_mark

def update_board_player_2(in_put,board,player_2_mark):
    board[in_put-1] = player_2_mark


#print board:
def print_board(board):
    print(f"{board[0]}|{board[1]}|{board[2]}")
    print("-----")
    print(f"{board[3]}|{board[4]}|{board[5]}")
    print("-----")
    print(f"{board[6]}|{board[7]}|{board[8]}")

#print rule board:
def print_rule_board():
    print(f"{'1'}|{'2'}|{'3'}")
    print("----")
    print(f"{'4'}|{'5'}|{'6'}")
    print("----")
    print(f"{'7'}|{'8'}|{'9'}")

#play_1 check win
def check_win_player_1(board,player_1_mark):
    if board[0]==board[1]==board[2]==player_1_mark:
        return True
    elif board[3]==board[4]==board[5]==player_1_mark:
        return True
    elif board[6] == board[7] == board[8] == player_1_mark:
        return True
    elif board[0] == board[3] == board[6] == player_1_mark:
        return True
    elif board[1] == board[4] == board[7] == player_1_mark:
        return True
    elif board[2] == board[5] == board[8] == player_1_mark:
        return True
    elif board[0] == board[4] == board[8] == player_1_mark:
        return True
    elif board[2] == board[4] == board[6] == player_1_mark:
        return True
    else:
        return False

#play_2 check win
def check_win_player_2(board, player_2_mark):
    if board[0] == board[1] == board[2] == player_2_mark:
        return True
    elif board[3] == board[4] == board[5] == player_2_mark:
        return True
    elif board[6] == board[7] == board[8] == player_2_mark:
        return True
    elif board[0] == board[3] == board[6] == player_2_mark:
        return True
    elif board[1] == board[4] == board[7] == player_2_mark:
        return True
    elif board[2] == board[5] == board[8] == player_2_mark:
        return True
    elif board[0] == board[4] == board[8] == player_2_mark:
        return True
    elif board[2] == board[4] == board[6] == player_2_mark:
        return True
    else:
        return False

#check tie
def check_tie(index):
    if len(index) == 9:
        return True
    else:
        return False

#check_play_again
def play_again_():
    in_put = ''
    while in_put not in ['no','yes']:
        in_put = (input("Do you want to play again ?no/yes: ")).lower()
    if in_put == 'yes':
        return 1
    elif in_put == 'no':
        return 0


play_again = 1
while play_again==1:
    print('\n'*10)
    player_1_mark = ''
    player_2_mark = ''

    board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    index = []
    in_put = ''
    player_1_mark,player_2_mark = welcome()
    while 1==1:
        print("Player 1 turn:")
        print_rule_board()
        print('\n')
        print_board(board)
        in_put = input_check(index)
        update_board_player_1(in_put,board,player_1_mark)
        if check_win_player_1(board,player_1_mark):
            print('\n' * 10)
            print("Player 1 win!!!!!!!!")
            print_board(board)
            play_again = play_again_()
            break
        elif check_win_player_2(board,player_2_mark):
            print('\n' * 10)
            print("Player 2 win!!!!!!!!!")
            print_board(board)
            play_again = play_again_()
            break
        elif check_tie(index):
            print('\n' * 10)
            print("Tieeeee!!!!!!!")
            print_board(board)
            play_again = play_again_()
            break
        print("Player 2 turn:")
        print_rule_board()
        print('\n')
        print_board(board)
        in_put = input_check(index)
        update_board_player_2(in_put,board,player_2_mark)
        if check_win_player_1(board,player_1_mark):
            print('\n' * 10)
            print("Player 1 win!!!!!!!!")
            print_board(board)
            play_again = play_again_()
            break
        elif check_win_player_2(board,player_2_mark):
            print('\n' * 10)
            print("Player 2 win!!!!!!!!!")
            print_board(board)
            play_again = play_again_()
            break
        elif check_tie(index):
            print('\n' * 10)
            print("Tieeeee!!!!!!!")
            print_board(board)
            play_again = play_again_()
            break


