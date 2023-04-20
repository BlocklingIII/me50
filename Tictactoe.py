"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    x = 0
    o = 0
    for row in board:
        for item in row:
            if item == X:
                x += 1
            elif item == O:
                o += 1
    if x > o:
        return O
    else:
        return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions = []
    for row in range(3):
        for item in range(3):
            if board[row][item] == EMPTY:
                actions.append((row, item))
    return actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    new = copy.deepcopy(board)
    print('n:', new, 'b:', board)
    if new[action[0]][action[1]] != EMPTY:
        raise Exception('Not a valid move !')
    new[action[0]][action[1]] = player(board)
    return new


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    if utility(board) == 1:
        return X
    elif utility(board) == -1:
        return O
    else:
        return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if utility(board) != None:
        return True
    else:
        return False

def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    for row in board:
        if row[0] == row[1] == row[2] != EMPTY:
            return isXorO(row[0])

    for i in range(3):
        if board[0][i] == board[1][i] == board[2][i] != EMPTY:
            return isXorO(board[0][i])

    if board[0][0] == board[1][1] == board[2][2] != EMPTY:
        return isXorO(board[0][0])

    if board[0][2] == board[1][1] == board[2][0] != EMPTY:
        return isXorO(board[0][2])

    for row in board:
        for item in row:
            if item == EMPTY:
                return None

    return 0
    
def isXorO(coord):
    if coord == X:
        return 1
    else:
        return -1

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    elif player(board) == X:
        v, move = max_value(board)
        return move
    else:
        v, move = min_value(board)
        return move

def max_value(board):
    if terminal(board):
        return utility(board), None
        
    v = -math.inf
    move = None
    for action in actions(board):
        value, act = min_value(result(board, action))
        if value > v:
            v = value
            move = action
            if v == 1:
                return v, move
    return v, move

def min_value(board):
    if terminal(board):
        return utility(board), None
    v = math.inf
    move = None
    for action in actions(board):
        value, act = max_value(result(board, action))
        if value < v:
            v = value
            move = action
            if v == -1:
                return v, move
    return v, move
