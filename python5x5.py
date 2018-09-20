import random

#attribution
#https://codereview.stackexchange.com/questions/113840/tictactoe-where-the-computer-plays-random-moves-against-itself
#  Tic Tac Toe

#  Board is laid out as:
#  0, 1,  2,  9 , 16
#  3, 4,  5,  10, 17
#  6, 7,  8,  11 ,18
# 12, 13, 14  15, 19
# 20, 21, 22, 23, 24
a = 1
b = 0
c= 0
d= 0
z = 1000000

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
        [0, 1, 2], [3, 4, 5], [6, 7, 8], [1,2,9], [4,5,10], [7,8,11], [12,13,14], [13,14,15], [2,9,16], [5,10,17], [8,11,18], [14,15,19],
        [22,23,24], [11,15,23], [8,14,22], [7,13,21], [6,12,20] ,  # Horizontal
        [0, 3, 6], [1, 4, 7], [2, 5, 8], [9,10,11], [3,6,12], [4,7,13], [5,8,14], [10,11,15], [16,17,18], [17,18,19], 
        [18,19,24], [11,15,23], [8,14,22], [7,13,21], [6,12,20],  # Vertical
        [0, 4, 8], [2, 4, 6], [5,7,9], [1,5,11], [4,8,15], [5,7,12], [20,13,8], [8,15,24], [16,10,8], 
        [11,14,17], [18,15,22], [6,13,22], [21,14,11]  # Diagonal
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
        for pos in range(25):
            if (board[pos] == 0):
                return None

        #game is a draw
        return 0

    def find_move(board, player):
        legal_moves = []

        for pos in range(25):
            if (board[pos] == 0):
                legal_moves.append(pos)

        return random.choice(legal_moves)

    def make_move(board, move, player):
        board[move] = player

    #def write_board(board):
        #letter = {0: '-', 1: 'X', 2: 'O'}
        #letter = "-XO"
        #for row in range(3):
            #for col in range(4):
                #print(letter[board[row*3+col]]),
            #print()
        #print()

    def play():
        board = []
        for pos in range(25):
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
                    cincrement()
                break
            player = 3 - player

    play()
    a = a+1
print(b)
print(c)
print(d)    