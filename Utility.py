from referee import *
import Node
import a_start_algorithm
def Utility(board, next_move, weights, game):
    return feature_1(board, next_move, game)*weights[0]+\
           feature_2(board, next_move, game)*weights[1]\
           +feature_3(board, next_move, game)*weights[2]\
           +feature_4(board, next_move, game)*weights[3]

#calculate the distance needed to reach the end
def feature_1(board, next_move, game):
    result = 0
    if game._turn_player == "red":
        for i in range(0,board.n):
            finish_coord = (board.n, i)
            result += a_start_algorithm(board, next_move, finish_coord)
        result = result % board.n
    elif game._turn_player == "blue":
        for i in range(0,board.n):
            finish_coord = (i, board.n)
            result += a_start_algorithm(board, next_move, finish_coord)
        result = result % board.n
    return float(result)


def feature_2(board, next_move, game):
    length = 0


def feature_3(board, next):


def feature_4(board):