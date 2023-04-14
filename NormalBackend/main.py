import asyncio
import json
import copy
import websockets
import Validator

clients = {}
#
# board = [
#
#     ['Cell', 'Cell', 'Cell', 'Cell', 'bKing', 'Cell', 'Cell', 'Cell'],
#     ['Cell', 'Cell', 'Cell', 'Cell', 'Cell', 'Cell', 'Cell', 'Cell'],
#     ['Cell', 'Cell', 'Cell', 'Cell', 'Cell', 'Cell', 'Cell', 'Cell'],
#     ['Cell', 'Cell', 'Cell', 'Cell', 'Cell', 'Cell', 'Cell', 'Cell'],
#     ['Cell', 'Cell', 'Cell', 'Cell', 'Cell', 'Cell', 'Cell', 'Cell'],
#     ['wRook', 'Cell', 'Cell', 'Cell', 'Cell', 'Cell', 'Cell', 'Cell'],
#     ['Cell', 'Cell', 'wRook', 'Cell', 'Cell', 'Cell', 'Cell', 'Cell'],
#     ['Cell', 'Cell', 'Cell', 'Cell', 'wKing', 'Cell', 'Cell', 'Cell'],
#
# ]
board = [
    ['bRook', 'bKnight', 'bBishop', 'bQueen', 'bKing', 'bBishop', 'bKnight', 'bRook'],
    ['bPawn', 'bPawn', 'bPawn', 'bPawn', 'bPawn', 'bPawn', 'bPawn', 'bPawn'],
    ['Cell', 'Cell', 'Cell', 'Cell', 'Cell', 'Cell', 'Cell', 'Cell'],
    ['Cell', 'Cell', 'Cell', 'Cell', 'Cell', 'Cell', 'Cell', 'Cell'],
    ['Cell', 'Cell', 'Cell', 'Cell', 'Cell', 'Cell', 'Cell', 'Cell'],
    ['Cell', 'Cell', 'Cell', 'Cell', 'Cell', 'Cell', 'Cell', 'Cell'],
    ['wPawn', 'wPawn', 'wPawn', 'wPawn', 'wPawn', 'wPawn', 'wPawn', 'wPawn'],
    ['wRook', 'wKnight', 'wBishop', 'wQueen', 'wKing', 'wBishop', 'wKnight', 'wRook']
]


def moving_check(moves):
    print(moves)
    moves = list(moves)
    x1 = int(moves[0])
    y1 = int(moves[1])
    x2 = int(moves[2])
    y2 = int(moves[3])

    new_board = copy.deepcopy(board)
    temp_piece = new_board[x1][y1]
    new_board[x1][y1] = 'Cell'
    new_board[x2][y2] = temp_piece

    return new_board


def moving(moves, color):
    moves = list(moves)
    x1 = int(moves[0])
    y1 = int(moves[1])

    x2 = int(moves[2])
    y2 = int(moves[3])
    temp_piece = board[x1][y1]

    if Validator.is_check(board):
        if Validator.is_check(moving_check(moves)):
            print('Ход невозможен moving()')
            return color
        else:
            board[x1][y1] = 'Cell'
            board[x2][y2] = temp_piece
            if x2 == 0 and temp_piece == 'wPawn':
                board[x2][y2] = 'wQueen'
            if x2 == 7 and temp_piece == 'bPawn':
                board[x2][y2] = 'bQueen'
            if color == 'white':
                color = 'black'
            else:
                color = 'white'
            return color
    elif not Validator.is_check(board):
        board[x1][y1] = 'Cell'
        board[x2][y2] = temp_piece

        if x2 == 0 and temp_piece == 'wPawn':
            board[x2][y2] = 'wQueen'
        if x2 == 7 and temp_piece == 'bPawn':
            board[x2][y2] = 'bQueen'
        if color == 'white':
            color = 'black'
        else:
            color = 'white'
        return color


def register(websocket, name, color):
    clients[color] = {'name': name, 'websocket': websocket}
    print(name, ' welcome')
    print('Список участников: ', clients.values())


async def send_message(color, moves):
    b_data = clients['black']
    b_ws = b_data['websocket']

    w_data = clients['white']
    w_ws = w_data['websocket']

    if color == 'white':
        coll = 'b'
    else:
        coll = 'w'

    color = moving(moves, color)
    print('Board в порядке')

    if Validator.is_checkmate(board, coll):
        print('checkmate')
        if color == 'white':
            c = 'black'
        else:
            c = 'white'
        await w_ws.send('checkmate:'+c)
        await b_ws.send('checkmate:'+c)

    await w_ws.send('move:' + color + ':' + json.dumps(board) + ':' + str(False))
    print('Отправлено: ', w_data['name'], moves)
    await b_ws.send('move:' + color + ':' + json.dumps(board) + ":" + str(False))
    print('Отправлено: ', b_data['name'], moves)


async def handle_socket(websocket, path):
    while True:
        try:
            message = await websocket.recv()
            commands = message.split(':')

            # 1 - reg, move, message
            # 2 - data
            # 3 - board if 1 == move

            # Register
            if commands[0] == 'reg':
                register(websocket, commands[1], commands[2])

            # SendMessage
            elif commands[0] == 'move':
                print('Move: ', commands)
                await send_message(commands[2], commands[1])

        except websockets.WebSocketException:
            break


async def main():
    # Создаем веб-сокет сервер и запускаем его на порту 5000
    server = await websockets.serve(handle_socket, '0.0.0.0', 9999)
    print('WebSocket server started on ws://localhost:9999')

    # Запускаем сервер в бесконечном цикле
    await server.wait_closed()


# Запускаем основной цикл асинхронного выполнения
asyncio.get_event_loop().run_until_complete(main())
