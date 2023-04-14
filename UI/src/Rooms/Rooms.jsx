import React, {useEffect, useState} from 'react';
import {useNavigate} from "react-router-dom";
import ChessBoard from "../ChessBoard";

const Room = ({color, roomId, password, name}) => {
    const [socket, setSocket] = useState(new WebSocket('ws://localhost:9999'));
    const [message, setMessage] = useState('');
    const [messages, setMessages] = useState([{}]);

    const nav = useNavigate();
    // const connect = () => {
    //     socket.addEventListener('message', (event) => {
    //         if (!event.data.includes('move')) {
    //             if (event.data === '401') {
    //                 alert('Данные не верны');
    //                 nav('/');
    //             } else if (event.data !== '200') {
    //                 console.log(event.data)
    //                 let temp = event.data.split(':');
    //                 setMessages(prevState => [prevState, {message: temp[1], author: temp[2]}]);
    //                 console.log('Получено сообщение от сервера:', event.data);
    //             }
    //         }
    //     });
    // }
    // useEffect(() => {
    //
    //
    //
    //
    // }, []);
    //
    //

// Отправляем сообщение на сервер
    const sendMessage = () => {
        socket.send(message);
    };


    return (
        <div>
            <h1>WebSocket Client</h1>
            <input
                value={message}
                placeholder="Сообщение"
                onChange={(e) => setMessage(e.target.value)}
            />
            <button onClick={sendMessage}>Отправить</button>
            {messages.map((mess,index) => <div key={index}><div>{mess.author}: {mess.message}</div><br/></div>)}
            <ChessBoard socket={socket} color={color}/>
        </div>
    );
};

export default Room;
