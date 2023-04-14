import React from 'react';

class Raw extends React.Component {

    static checkMoveability(x1, y1, x2, y2, data){
        const color = data[x1][y1].substring(0,1);
        const piece = data[x1][y1].substring(1);

        if(piece === 'Pawn'){
            return this.pawnMoveability(x1,y1,x2,y2,data,color);
        }
        if(piece === 'Bishop'){
            return this.bishopMoveability(x1,y1,x2,y2,data,color);
        }
        if(piece === 'Rook'){
            return this.rookMoveability(x1,y1,x2,y2,data,color);
        }
        if(piece === 'Knight'){
            return this.knightMoveability(x1,y1,x2,y2,data,color);
        }
        if(piece === 'Queen'){
            return this.queenMoveability(x1,y1,x2,y2,data,color);
        }
        if(piece === 'King'){
            return this.kingMoveability(x1,y1,x2,y2,data,color);
        }
        return false; // Возвращаем false, если ход невозможен
    };
    static pawnMoveability(x1, y1, x2, y2, data, color) {
        if (color === 'w') { // Если цвет пешки белый

            if (x2 === x1 - 1 && y2 === y1) { // Проверяем возможность хода на одну клетку вперед

                if (data[x2][y2] === 'Cell') { // Проверяем, что целевая клетка свободна

                    return true; // Возвращаем true, если ход возможен
                }
            }
            else if (x2 === x1 - 2 && y2 === y1 && x1 === 6 && data[x2][y2] === 'Cell' && data[x1 - 1][y1] === 'Cell') { // Проверяем возможность двойного хода в начале игры
                return true;
            }

            else if (x1 === x2 + 1 && (y2 === y1 - 1 || y2 === y1 + 1)) {

                if (data[x2][y2].substring(0, 1) === 'b') { // Проверяем, что на целевой клетке находится фигура противоположного цвета или пешка, сделавшая двойной ход
                    return true; // Возвращаем true, если ход возможен
                }
            }
        }
        else if (color === 'b') { // Если цвет пешки черный
            console.log('eat')
            if (x2 === x1 + 1 && y2 === y1) { // Проверяем возможность хода на одну клетку вперед
                if (data[x2][y2] === 'Cell') { // Проверяем, что целевая клетка свободна
                    return true; // Возвращаем true, если ход возможен
                }
            }
            else if (x2 === x1 + 2 && y2 === y1 && x1 === 1 && data[x2][y2] === 'Cell' && data[x1 + 1][y1] === 'Cell') { // Проверяем возможность двойного хода в начале игры
                return true;
            }
            else if (x1 === x2-1 && (y2 === y1 - 1 || y2 === y1 + 1) && (data[x2][y2].substring(0, 1) === 'w' || (data[x2][y2].substring(1) === 'Pawn' && data[x2][y2].includes('doubleMove')))) { // Проверяем возможность хода на диагональ
                // Проверяем, что на целевой клетке находится фигура противоположного цвета или пешка, сделавшая двойной ход
                return true; // Возвращаем true, если ход возможен
            }
        }

        return false; // Возвращаем false, если ход невозможен
    }
    static bishopMoveability(x1, y1, x2, y2, data, color){
        const dx = Math.abs(x2 - x1);
        const dy = Math.abs(y2 - y1);

        if (dx === dy) { // Проверяем, что ход по диагонали

            const xDir = x2 > x1 ? 1 : -1;
            const yDir = y2 > y1 ? 1 : -1;

            let i = x1 + xDir;
            let j = y1 + yDir;

            while (i !== x2 && j !== y2) { // Проверяем, что между начальной и конечной клетками нет других фигур
                if (data[i][j] !== 'Cell') {
                    return false; // Возвращаем false, если на пути слона есть другая фигура
                }
                i += xDir;
                j += yDir;
            }

            if (data[x2][y2] === 'Cell' || data[x2][y2].startsWith(color === 'w' ? 'b' : 'w')) { // Проверяем, что на конечной клетке либо свободная клетка, либо фигура противоположного цвета
                return true; // Возвращаем true, если ход возможен
            }
        }

        return false; // Возвращаем false, если ход невозможен
    }
    static rookMoveability(x1, y1, x2, y2, data, color){
        if (x1 === x2 || y1 === y2) { // Проверяем, что ладья двигается по вертикали или горизонтали
            const xDir = x1 === x2 ? 0 : (x2 > x1 ? 1 : -1);
            const yDir = y1 === y2 ? 0 : (y2 > y1 ? 1 : -1);

            let i = x1 + xDir;
            let j = y1 + yDir;

            while (i !== x2 || j !== y2) { // Проверяем, что между начальной и конечной клетками нет других фигур
                if (data[i][j] !== 'Cell') {
                    return false; // Возвращаем false, если на пути ладьи есть другая фигура
                }
                i += xDir;
                j += yDir;
            }

            if (data[x2][y2] === 'Cell' || data[x2][y2].startsWith(color === 'w' ? 'b' : 'w')) { // Проверяем, что на конечной клетке либо свободная клетка, либо фигура противоположного цвета
                return true; // Возвращаем true, если ход возможен
            }
        }

        return false; // Возвращаем false, если ход невозможен
    }
    static knightMoveability(x1, y1, x2, y2, data, color){
        const dx = Math.abs(x2 - x1);
        const dy = Math.abs(y2 - y1);

        // Проверяем, что конь перемещается "буквой Г", т.е. одна координата изменяется на 2, другая на 1, или наоборот
        if ((dx === 1 && dy === 2) || (dx === 2 && dy === 1)) {
            if (data[x2][y2] === 'Cell' || data[x2][y2].startsWith(color === 'w' ? 'b' : 'w')) { // Проверяем, что на конечной клетке либо свободная клетка, либо фигура противоположного цвета
                return true; // Возвращаем true, если ход возможен
            }
        }

        return false; // Возвращаем false, если ход невозможен
    }
    static queenMoveability(x1, y1, x2, y2, data, color){
        const dx = Math.abs(x2 - x1);
        const dy = Math.abs(y2 - y1);

        // Проверяем, что ход ферзя может быть выполнен как ход слона или ладьи
        if ((dx === dy) || (x1 === x2 || y1 === y2)) {
            if (this.bishopMoveability(x1, y1, x2, y2, data, color) || this.rookMoveability(x1, y1, x2, y2, data, color)) { // Проверяем, что ход ферзя может быть выполнен как ход слона или ладьи
                return true; // Возвращаем true, если ход возможен
            }
        }

        return false; // Возвращаем false, если ход невозможен
    }
    static kingMoveability(x1, y1, x2, y2, data, color){
        const dx = Math.abs(x2 - x1);
        const dy = Math.abs(y2 - y1);

        // Проверяем, что король может сделать ход на одну клетку в любом направлении
        if ((dx <= 1) && (dy <= 1)) {
            return true; // Возвращаем true, если ход возможен
        }

        return false; // Возвращаем false, если ход невозможен
    }
}

export default Raw;
