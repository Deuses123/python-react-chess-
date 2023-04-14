def check_moveability(x1, y1, x2, y2, data):
    color = data[x1][y1][0:]
    piece = data[x1][y1][1:]

    if piece == 'Pawn':
        return pawn_moveability(x1, y1, x2, y2, data, color)
    if piece == 'Bishop':
        return bishop_moveability(x1, y1, x2, y2, data, color)
    if piece == 'Rook':
        return rook_moveability(x1, y1, x2, y2, data, color)
    if piece == 'Knight':
        return knight_moveability(x1, y1, x2, y2, data, color)
    if piece == 'Queen':
        return queen_moveability(x1, y1, x2, y2, data, color)
    if piece == 'King':
        return king_moveability(x1, y1, x2, y2, data)
    return False  # Возвращаем False, если ход невозможен

def knight_moveability(x1, y1, x2, y2, data, color):
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)

    # Проверяем, что конь перемещается "буквой Г", т.е. одна координата изменяется на 2, другая на 1, или наоборот
    if (dx == 1 and dy == 2) or (dx == 2 and dy == 1):
        if data[x2][y2] == 'Cell' or data[x2][y2].startswith('b' if color == 'w' else 'w'):  # Проверяем, что на конечной клетке либо свободная клетка, либо фигура противоположного цвета
            return True  # Возвращаем True, если ход возможен

    return False  # Возвращаем False, если ход невозможен

def pawn_moveability(x1, y1, x2, y2, data, color):
    if color == 'w': # Если цвет пешки белый
        if x2 == x1 - 1 and y2 == y1: # Проверяем возможность хода на одну клетку вперед
            if data[x2][y2] == 'Cell': # Проверяем, что целевая клетка свободна
                return True # Возвращаем True, если ход возможен
        elif x2 == x1 - 2 and y2 == y1 and x1 == 6 and data[x2][y2] == 'Cell' and data[x1 - 1][y1] == 'Cell': # Проверяем возможность двойного хода в начале игры
            return True
        elif x1 == x2 + 1 and (y2 == y1 - 1 or y2 == y1 + 1):
            if data[x2][y2][:1] == 'b': # Проверяем, что на целевой клетке находится фигура противоположного цвета или пешка, сделавшая двойной ход
                return True # Возвращаем True, если ход возможен
    elif color == 'b': # Если цвет пешки черный
        if x2 == x1 + 1 and y2 == y1: # Проверяем возможность хода на одну клетку вперед
            if data[x2][y2] == 'Cell': # Проверяем, что целевая клетка свободна
                return True # Возвращаем True, если ход возможен
        elif x2 == x1 + 2 and y2 == y1 and x1 == 1 and data[x2][y2] == 'Cell' and data[x1 + 1][y1] == 'Cell': # Проверяем возможность двойного хода в начале игры
            return True
        elif x1 == x2 - 1 and (y2 == y1 - 1 or y2 == y1 + 1) and (data[x2][y2][:1] == 'w' or (data[x2][y2][1:] == 'Pawn' and 'doubleMove' in data[x2][y2])): # Проверяем возможность хода на диагональ
            # Проверяем, что на целевой клетке находится фигура противоположного цвета или пешка, сделавшая двойной ход
            return True # Возвращаем True, если ход возможен
    return False # Возвращаем False, если ход невозможен

def bishop_moveability(x1, y1, x2, y2, data, color):
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)

    if dx == dy:  # Проверяем, что ход по диагонали
        x_dir = 1 if x2 > x1 else -1
        y_dir = 1 if y2 > y1 else -1

        i = x1 + x_dir
        j = y1 + y_dir

        while i != x2 and j != y2:  # Проверяем, что между начальной и конечной клетками нет других фигур
            if data[i][j] != 'Cell':
                return False  # Возвращаем False, если на пути слона есть другая фигура
            i += x_dir
            j += y_dir

        if data[x2][y2] == 'Cell' or data[x2][y2].startswith('b' if color == 'w' else 'w'):  # Проверяем, что на конечной клетке либо свободная клетка, либо фигура противоположного цвета
            return True  # Возвращаем True, если ход возможен

    return False  # Возвращаем False, если ход невозможен

def rook_moveability(x1, y1, x2, y2, data, color):
    if x1 == x2 or y1 == y2:  # Проверяем, что ладья двигается по вертикали или горизонтали
        x_dir = 0 if x1 == x2 else (1 if x2 > x1 else -1)
        y_dir = 0 if y1 == y2 else (1 if y2 > y1 else -1)

        i = x1 + x_dir
        j = y1 + y_dir

        while i != x2 or j != y2:  # Проверяем, что между начальной и конечной клетками нет других фигур
            if data[i][j] != 'Cell':
                return False  # Возвращаем False, если на пути ладьи есть другая фигура
            i += x_dir
            j += y_dir

        if data[x2][y2] == 'Cell' or data[x2][y2].startswith('b' if color == 'w' else 'w'):  # Проверяем, что на конечной клетке либо свободная клетка, либо фигура противоположного цвета
            return True  # Возвращаем True, если ход возможен

    return False  # Возвращаем False, если ход невозможен

def rook_moveability(x1, y1, x2, y2, data, color):
    if x1 == x2 or y1 == y2:  # Проверяем, что ладья двигается по вертикали или горизонтали
        x_dir = 0 if x1 == x2 else (1 if x2 > x1 else -1)
        y_dir = 0 if y1 == y2 else (1 if y2 > y1 else -1)

        i = x1 + x_dir
        j = y1 + y_dir

        while i != x2 or j != y2:  # Проверяем, что между начальной и конечной клетками нет других фигур
            if data[i][j] != 'Cell':
                return False  # Возвращаем False, если на пути ладьи есть другая фигура
            i += x_dir
            j += y_dir

        if data[x2][y2] == 'Cell' or data[x2][y2].startswith('b' if color == 'w' else 'w'):  # Проверяем, что на конечной клетке либо свободная клетка, либо фигура противоположного цвета
            return True  # Возвращаем True, если ход возможен

    return False  # Возвращаем False, если ход невозможен

def queen_moveability(x1, y1, x2, y2, data, color):
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)

    # Проверяем, что ход ферзя может быть выполнен как ход слона или ладьи
    if dx == dy or x1 == x2 or y1 == y2:
        if bishop_moveability(x1, y1, x2, y2, data, color) or rook_moveability(x1, y1, x2, y2, data, color):
            # Проверяем, что ход ферзя может быть выполнен как ход слона или ладьи
            return True  # Возвращаем True, если ход возможен

    return False  # Возвращаем False, если ход невозможен

def king_moveability(x1, y1, x2, y2, data):
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    color = data[x1][y1][0]
    # Проверяем, что король может сделать ход на одну клетку в любом направлении
    if dx <= 1 and dy <= 1:
        # Проверяем, что на конечной клетке нет своей фигуры
        if data[x2][y2] is None or not data[x2][y2].startswith(color):
            return True  # Возвращаем True, если ход возможен

    return False  # Возвращаем False, если ход невозможен
