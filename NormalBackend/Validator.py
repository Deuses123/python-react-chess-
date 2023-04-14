def is_check(board):
    """
    Функция для проверки наличия шаха на шахматной доске.
    :param board: Двумерный массив, представляющий шахматную доску.
    :return: True, если есть шах, False в противном случае.
    """
    # Координаты короля
    king_row = None
    king_col = None

    # Поиск координат короля
    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col] == 'wKing':  # Используем 'wKing' как маркер белого короля
                king_row = row
                king_col = col
                break

    if king_row is None or king_col is None:
        # Белого короля не найдено, ошибка в доске
        raise ValueError("Ошибка: Белый король не найден на доске!")

    # Проверка наличия шаха по направлениям ферзя, ладью, слона и коня
    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col] != 'Cell' and board[row][col] != 'wKing':  # Игнорируем пустые клетки и белого короля
                piece = board[row][col]
                if piece == 'bQueen' or piece == 'bRook':
                    # Проверка наличия шаха по направлениям ферзя и ладьи
                    if row == king_row or col == king_col or abs(row - king_row) == abs(col - king_col):
                        return True
                elif piece == 'bBishop':
                    # Проверка наличия шаха по диагонали
                    if abs(row - king_row) == abs(col - king_col):
                        return True
                elif piece == 'bKnight':
                    # Проверка наличия шаха от коня
                    if abs(row - king_row) == 2 and abs(col - king_col) == 1 or \
                       abs(row - king_row) == 1 and abs(col - king_col) == 2:
                        return True

    return False


board = [
    ['bRook', 'bKnight', 'bBishop', 'bQueen', 'bKing', 'bBishop', 'bKnight', 'bRook'],
    ['bPawn', 'bPawn',   'bPawn',   'bPawn',  'bPawn', 'bPawn',   'bPawn',   'bPawn'],
    ['Cell',  'Cell',    'Cell',    'Cell',   'Cell', 'Cell',     'Cell',     'Cell'],
    ['Cell',  'Cell',    'Cell',    'Cell',   'Cell',  'Cell',    'Cell',    'Cell'],
    ['Cell',  'Cell',    'Cell',    'Cell',   'Cell',  'Cell',    'Cell',    'Cell'],
    ['Cell',  'Cell',    'Cell',    'Cell',   'Cell',  'Cell',    'Cell',    'Cell'],
    ['wPawn', 'wPawn',   'wPawn',   'wPawn',  'Cell',  'Cell',    'wPawn',   'wPawn'],
    ['wRook', 'wKnight', 'wBishop', 'wQueen', 'wKing', 'wBishop', 'wKnight', 'wRook']
]

print(is_check(board))  # Выведет True, указывая на наличие шаха белому королю


