import React, {useState} from 'react';
import {useNavigate} from "react-router-dom";

const Game = ({socket,color, setColor}) => {
    const [name, setName] = useState('');

    // Обработчик изменения значения чекбокса
    const handleCheckboxChange = (color) => {;
        setColor(color);
    };
    const nav = useNavigate();
    const connect = () => {
        socket.send(`reg:${name}:${color}`)
        nav('/game');
    }

    return (
        <div>
            <input value={name} onChange={e => setName(e.target.value)} placeholder='Введите имя'/>
            <br/>Выберите цвет<br/>
            <input
                type="checkbox"
                checked={color === 'white'}
                onChange={()=>handleCheckboxChange('white')}
            />
            <br/>
            <input
                type="checkbox"
                checked={color === 'black'}
                onChange={()=> handleCheckboxChange('black')}
            />
            <br/>

            <button onClick={connect}>Подключиться</button>

        </div>
    );
};

export default Game;
