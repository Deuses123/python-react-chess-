from pprint import pprint
import copy as c

import Check_moves


def find_king(data, color):
    for row in range(8):
        for col in range(8):
            if data[row][col] == color + 'King':
                return row, col


def is_check(board):
    white_king_row, white_king_col = None, None
    black_king_row, black_king_col = None, None

    for row in range(8):
        for col in range(8):
            piece = board[row][col]
            if piece == 'wKing':
                white_king_row, white_king_col = row, col
            elif piece == 'bKing':
                black_king_row, black_king_col = row, col

    for row in range(8):
        for col in range(8):
            piece = board[row][col]
            if piece.startswith('b'):
                if piece == 'bPawn':
                    if (row + 1 == white_king_row and abs(col - white_king_col) == 1):
                        return True
                elif piece == 'bKing':
                    if abs(row - white_king_row) <= 1 and abs(col - white_king_col) <= 1:
                        return True
                elif piece == 'bKnight':
                    if (abs(row - white_king_row) == 2 and abs(col - white_king_col) == 1) or \
                            (abs(row - white_king_row) == 1 and abs(col - white_king_col) == 2):
                        return True
                elif piece == 'bRook':
                    if row == white_king_row or col == white_king_col:
                        if not is_piece_between(row, col, white_king_row, white_king_col, board):
                            return True
                elif piece == 'bQueen':
                    if row == white_king_row or col == white_king_col:
                        if not is_piece_between(row, col, white_king_row, white_king_col, board):
                            return True
                    if abs(row - white_king_row) == abs(col - white_king_col):
                        if not is_piece_between(row, col, white_king_row, white_king_col, board):
                            return True

                elif piece == 'bBishop':
                    if abs(row - white_king_row) == abs(col - white_king_col):
                        if not is_piece_between(row, col, white_king_row, white_king_col, board):
                            return True

    for row in range(8):
        for col in range(8):
            piece = board[row][col]
            if piece.startswith('w'):
                if piece == 'wPawn':
                    if row - 1 == black_king_row and abs(col - black_king_col) == 1:
                        return True
                elif piece == 'wKing':
                    if abs(row - black_king_row) <= 1 and abs(col - black_king_col) <= 1:
                        return True
                elif piece == 'wKnight':
                    if (abs(row - black_king_row) == 2 and abs(col - black_king_col) == 1) or \
                            (abs(row - black_king_row) == 1 and abs(col - black_king_col) == 2):
                        return True
                elif piece == 'wRook':
                    if row == black_king_row or col == black_king_col:
                        if not is_piece_between(row, col, black_king_row, black_king_col, board):
                            return True

                elif piece == 'wQueen':
                    if row == black_king_row or col == black_king_col:
                        if not is_piece_between(row, col, black_king_row, black_king_col, board):
                            return True
                    if abs(row - black_king_row) == abs(col - black_king_col):
                        if not is_piece_between(row, col, black_king_row, black_king_col, board):
                            return True

                elif piece == 'wBishop':
                    if abs(row - black_king_row) == abs(col - black_king_col):
                        if not is_piece_between(row, col, black_king_row, black_king_col, board):
                            return True

    return False


def is_piece_between(start_row, start_col, end_row, end_col, board):
    step_row = 0 if start_row == end_row else (1 if start_row < end_row else -1)
    step_col = 0 if start_col == end_col else (1 if start_col < end_col else -1)
    row, col = start_row + step_row, start_col + step_col
    while row != end_row or col != end_col:
        if board[row][col] != 'Cell':
            return True
        row += step_row
        col += step_col
    return False


temp_data = []


def moving(x1, y1, x2, y2, data):
    new_board = c.deepcopy(data)
    temp_piece = new_board[x1][y1]
    new_board[x1][y1] = 'Cell'
    new_board[x2][y2] = temp_piece
    return new_board


def is_checkmate(data, color):
    pprint(data)
    # Проверяем наличие шаха
    if is_check(data):
        # Проходим по всем клеткам на доске
        for x1 in range(8):
            for y1 in range(8):
                if data[x1][y1].startswith(color):
                    for x2 in range(8):
                        for y2 in range(8):
                            if Check_moves.check_moveability(x1, y1, x2, y2, data):
                                new_data = moving(x1, y1, x2, y2, data)
                                if not is_check(new_data):
                                    print(x1, y1, x2, y2)
                                    return False
        return True
    else:
        return False


bo = [['bRook', 'Cell', 'bBishop', 'bQueen', 'bKing', 'bBishop', 'bKnight', 'bRook'],
      ['Cell', 'bPawn', 'bPawn', 'bPawn', 'Cell', 'wQueen', 'bPawn', 'bPawn'],
      ['bPawn', 'Cell', 'bKnight', 'Cell', 'Cell', 'Cell', 'Cell', 'Cell'],
      ['Cell', 'Cell', 'Cell', 'Cell', 'bPawn', 'Cell', 'Cell', 'Cell'],
      ['Cell', 'Cell', 'wBishop', 'Cell', 'wPawn', 'Cell', 'Cell', 'Cell'],
      ['Cell', 'Cell', 'Cell', 'Cell', 'Cell', 'Cell', 'Cell', 'Cell'],
      ['wPawn', 'wPawn', 'wPawn', 'wPawn', 'Cell', 'wPawn', 'wPawn', 'wPawn'],
      ['wRook', 'wKnight', 'wBishop', 'Cell', 'wKing', 'Cell', 'wKnight', 'wRook']]