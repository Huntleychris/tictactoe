import random

#  Tic Tac Toe
#attribution
#https://codereview.stackexchange.com/questions/113840/tictactoe-where-the-computer-plays-random-moves-against-itself
#  Board is laid out as:
#  0, 1, 2,
#  3, 4, 5,
#  6, 7, 8
a = 1
b = 0
c= 0
d= 0
z = 100000

def aincrement():
    global b
    b = b+1

def bincrement():
    global c
    c = c+1

def cincrement():
    global d
    d = d+1

while a < z:

    winning_rows = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],    # Horizontal
        [0, 3, 6], [1, 4, 7], [2, 5, 8],    # Vertical
        [0, 4, 8], [2, 4, 6]                # Diagonal
    ]
    def check_winner(board):
        for player in [1, 2]:
            for seq in winning_rows:
                for pos in seq:
                    if (board[pos]!=player):
                        break
                else:
                    return player

        #nobody won, check for draw (return 0 for draw, None for incomplete game)
        for pos in range(9):
            if (board[pos] == 0):
                return None

        #game is a draw
        return 0

    def find_move(board, player):
        legal_moves = []

        for pos in range(9):
            if (board[pos] == 0):
                legal_moves.append(pos)

        return random.choice(legal_moves)

    def make_move(board, move, player):
        board[move] = player

    def write_board(board):
        #letter = {0: '-', 1: 'X', 2: 'O'}
        letter = "-XO"
        for row in range(3):
            for col in range(3):
                print(letter[board[row*3+col]]),
            print()
        print()

    def play():
        board = []
        for pos in range(9):
            board.append(0)

        #write_board(board)  

        player = 1
        while True:
            move = find_move(board, player)
            make_move(board, move, player)
            #write_board(board)
            winner = check_winner(board)
            if winner != None:
                if winner == 1:
                    aincrement()
                if winner == 2:
                    bincrement()
                if winner == 0:
                  