import {useState} from "react";
import {Route, Routes} from "react-router-dom";
import './ChessBoard.css';
import ChessBoard from "./ChessBoard";
import Game from "./Game";

function App() {
    const [socket] = useState(new WebSocket('ws://localhost:9999'));
    const [color, setColor] = useState('');
    return (

        <div className="App">
            <Routes>
                <Route path='/' element={<Game socket={socket} setColor={setColor} color = {color} />}/>
                <Route path="/game" element={<ChessBoard color={color} socket={socket} />}/>
            </Routes>
        </div>

    );
}

export default App;
