from library import *
if __name__ == "__main__":
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
            if check_win_player_2(board,player_2_mark):
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


