import math
import numpy as np
import random

n_row, n_col = 8, 8


def count_nearby_bombs(pos, board):
    nearby_bombs = 0
    if pos[0] > 0 and pos[1] > 0 and board[pos[0]-1][pos[1]-1] == 'X':
        nearby_bombs += 1
    if pos[0] > 0 and board[pos[0]-1][pos[1]] == 'X':
        nearby_bombs += 1
    if pos[0] > 0 and pos[1] < board.shape[1] - 1 and board[pos[0]-1][pos[1]+1] == 'X':
        nearby_bombs += 1
    if pos[1] > 0 and board[pos[0]][pos[1]-1] == 'X':
        nearby_bombs += 1
    if pos[1] < board.shape[1] - 1 and board[pos[0]][pos[1]+1] == 'X':
        nearby_bombs += 1
    if pos[0] < board.shape[0] - 1 and pos[1] > 0 and board[pos[0]+1][pos[1]-1] == 'X':
        nearby_bombs += 1
    if pos[0] < board.shape[0] - 1 and board[pos[0]+1][pos[1]] == 'X':
        nearby_bombs += 1
    if pos[0] < board.shape[0] - 1 and pos[1] < board.shape[1] - 1 and board[pos[0]+1][pos[1]+1] == 'X':
        nearby_bombs += 1
    return nearby_bombs


def generate_board(pos, n_bombs, board_shape=(n_row, n_col)):
    board = np.empty(board_shape, str)  # Inicjalizacja planszy
    pos_id = pos[0] * board_shape[1] + pos[1]  # Indeks pozycji pierwszego (bezpiecznego) strzału gracza
    # Wygenerowanie indeksów pozycji bomb:
    avail_positions = [i for i in range(board.size) if i != pos_id]
    bomb_positions = random.sample(avail_positions, n_bombs)
    # Umieszczenie bomb na planszy:
    for bomb_pos in bomb_positions:
        x = math.floor(bomb_pos / board_shape[1])
        y = bomb_pos - x * board_shape[1]
        board[x][y] = 'X'
    # Uzupełnienie pozostałych pól planszy:
    for i in range(board_shape[0]):
        for j in range(board_shape[1]):
            if board[i][j] != 'X':
                board[i][j] = count_nearby_bombs(pos=(i, j), board=board)
    return board


def initialize_game(board_shape=(n_row, n_col)):
    # Inicjalizacja stanu planszy
    game = np.empty(board_shape, str)
    for i in range(board_shape[0]):
        for j in range(board_shape[1]):
            game[i][j] = '?'
    return game


print(generate_board(pos=(0, 0), n_bombs=25))
