import React from "react";
import Pieces from "./pieces/Pieces";
import './ChessCell.css'
import Raw from "./PieceRaw/Raw";

const ChessTypes = {
    'bPawn': <div className='piece'><Pieces type={'bP'}/></div>,
    'bRook':  <div className='piece'><Pieces type={'bR'}/></div>,
    'bKnight':  <div className='piece'><Pieces type={'bN'}/></div>,
    'bBishop':  <div className='piece'><Pieces type={'bB'}/></div>,
    'bQueen':  <div className='piece'><Pieces type={'bQ'}/></div>,
    'bKing':  <div className='piece'><Pieces type={'bK'}/></div>,
    'bCell':  '',
    'wPawn':  <div className='piece'><Pieces type={'wP'}/></div>,
    'wRook':  <div className='piece'><Pieces type={'wR'}/></div>,
    'wKnight':  <div className='piece'><Pieces type={'wN'}/></div>,
    'wBishop':  <div className='piece'><Pieces type={'wB'}/></div>,
    'wQueen':  <div className='piece'><Pieces type={'wQ'}/></div>,
    'wKing':  <div className='piece'><Pieces type={'wK'}/></div>,
    'wCell': '',
};


const ChessCell = ({checkMove, color, PreMove, squareColor, type, row, col, moveStatus, setPremove, setCurrentMove, setMove, piecesData}) => {

    const knightStyle = {
        backgroundColor: squareColor,
        color: type.substring(0,1) === 'b' ? 'black' : 'white',
        width: 50,
        height: 50,
        textAlign: 'center',
    };

    const validateMove = () => {
        color = color.substring(0,1)
        const moveId = piecesData[row][col].substring(0,1);

        if (piecesData[row][col].substring(0,1) === color || (PreMove.row !== null && PreMove.col !== null)){
            if(moveStatus === 'Empty' ){
                if (piecesData[row][col].substring(0,1) === 'w' || piecesData[row][col].substring(0,1) === 'b') {
                    setPremove({row: row, col: col});
                    setMove('PreMove')
                }
            }
            else if(moveStatus === 'PreMove'){
                if(piecesData[row][col].substring(0,1) === 'w' && piecesData[row][col].substring(0,1) === 'b' ){
                    setPremove({row: row, col: col})
                }

                if(Raw.checkMoveability(PreMove.row, PreMove.col, row, col, piecesData)) {
                    setCurrentMove({row: row, col: col});
                    setMove('CurrentMove')
                }

            }
            else if(moveStatus === 'CurrentMove'){

                setPremove({row: row, col: col});
                setMove('PreMove');
            }

        }

    }

    return <div className="chess-cell " style={knightStyle} onClick={validateMove}>{ChessTypes[type]}</div>;
};
export default ChessCell;