import React, {useEffect, useState} from 'react';
import './ChessBoard.css';
import ChessCell from "./ChessCell";
import Raw from './PieceRaw/Raw'

const ChessBoard = ({socket, color}) => {

    const [piecesData, setPiecesData] = useState([
        ['bRook', 'bKnight', 'bBishop', 'bQueen', 'bKing', 'bBishop', 'bKnight', 'bRook'],
        ['bPawn', 'bPawn', 'bPawn', 'bPawn', 'bPawn', 'bPawn', 'bPawn', 'bPawn'],
        ['Cell', 'Cell', 'Cell', 'Cell', 'Cell', 'Cell', 'Cell', 'Cell'],
        ['Cell', 'Cell', 'Cell', 'Cell', 'Cell', 'Cell', 'Cell', 'Cell'],
        ['Cell', 'Cell', 'Cell', 'Cell', 'Cell', 'Cell', 'Cell', 'Cell'],
        ['Cell', 'Cell', 'Cell', 'Cell', 'Cell', 'Cell', 'Cell', 'Cell'],
        ['wPawn', 'wPawn', 'wPawn', 'wPawn', 'wPawn', 'wPawn', 'wPawn', 'wPawn'],
        ['wRook', 'wKnight', 'wBishop', 'wQueen', 'wKing', 'wBishop', 'wKnight', 'wRook']
    ]);
    const [moveStatus, setMoveStatus] = useState('Empty')
    const [preMove, setPreMove] = useState({row: null, col:null});
    const [currentMove, setCurrentMove] = useState({row: null, col: null});
    const [previousPiecesData, setPreviousPiecesData] = useState(null);
    const [checkMove, setCheckMove] = useState('white');

    useEffect(() => {
        socket.addEventListener('message', (event) => {
            const message = event.data.split(':');
            if (message[0] === 'move') {
                const kingCheck = message[3]
                console.log(kingCheck)
                if(kingCheck !== 'True') {
                    setPiecesData(prevPiecesData => {
                        const tempData = JSON.parse(message[2]);
                        setMoveStatus('Empty');
                        setCurrentMove({col: null, row: null});
                        setPreMove({col: null, row: null});
                        setCheckMove(message[1]);
                        return tempData;
                    });
                }
                else {
                    alert('Король под шахом !!!');
                    setMoveStatus('Empty');
                    setCurrentMove({col: null, row: null});
                    setPreMove({col: null, row: null});
                    setCheckMove(message[1]);
                }
            }
        });
    }, []);


    useEffect(() => {
        if(moveStatus!=='Empty'){
            if(moveStatus==='CurrentMove') {
                // console.log(checkMove)
                if(checkMove === color) {
                    if (Raw.checkMoveability(preMove.row, preMove.col, currentMove.row, currentMove.col, piecesData)) {
                        socket.send(`move:${preMove.row}${preMove.col}${currentMove.row}${currentMove.col}:${color}`)
                        // setPiecesData(prevPiecesData => {
                        //     const tempData = JSON.parse(JSON.stringify(prevPiecesData));
                        //     const pie = tempData[preMove.row][preMove.col];
                        //     tempData[preMove.row][preMove.col] = 'Cell';
                        //     tempData[currentMove.row][currentMove.col] = pie;
                        //     setMoveStatus('Empty');
                        //     setCurrentMove({ col: null, row: null });
                        //     setPreMove({ col: null, row: null });
                        //     setCheckMove(color === 'white' ? 'black' : 'white');
                        //     return tempData;
                        // });
                    }
                }
                else {
                    console.log('Не твой ход дядя ходят ', checkMove)
                    setMoveStatus('Empty');
                    setCurrentMove({col: null, row: null})
                    setPreMove({col: null, row: null})
                }
            }

        }

    }, [moveStatus]);






    const isEven = (num) => num % 2 === 0;

    return (
        <div className="chess-board">
            {piecesData.map((rowData, row) => {
                return rowData.map((pieceData, col) => {
                    let squareColor = isEven(row + col) ? "#FFF0A3" : "#AB9163";
                    if(col === preMove.col && row === preMove.row){
                        squareColor = 'green';
                    }

                    if(currentMove.row === row && currentMove.col === col){
                        squareColor = 'purple'
                    }
                    return (
                        <ChessCell
                            checkMove = {checkMove}
                            color = {color}
                            key={`${row}${col}`}
                            piecesData={piecesData}
                            row={row}
                            col={col}
                            squareColor={squareColor}
                            type={pieceData}
                            setPiecesData={setPiecesData}
                            setMove={setMoveStatus}
                            setCurrentMove={setCurrentMove}
                            setPremove={setPreMove}
                            moveStatus={moveStatus}
                            PreMove={preMove}
                            CurrentMove={currentMove}
                        />
                    );
                });
            })}
        </div>
    );
};

export default ChessBoard;
